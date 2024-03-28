import os
import pkgutil
import importlib
from decimal import Decimal
from dotenv import load_dotenv
import logging
import logging.config
from app.commands.history_manger import HistoryManager


def configure_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    logging_conf_path = "logging.conf"
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
    logging.info("Logging configured.")


def main():
    configure_logging()
    load_dotenv()
    history_manager = HistoryManager(os.getenv("HIST_DIREC"))
    while True:
        plugins_dir = "app/plugins"
        print("\nMain Menu:")
        c = 1
        for item in os.listdir(plugins_dir):
            item_path = os.path.join(plugins_dir, item)
            if os.path.isdir(item_path):
                print(f"{c}. {item}")
                c += 1

        choice = input("Enter your choice (calc, history, exit): ").lower().strip()
        if choice == "exit":
            logging.info("Exiting...")
            break
        elif choice == "calc":
            if command_menu(history_manager, "Calculator"):
                break
        elif choice == "history":
            if command_menu(history_manager, "History"):
                break
        else:
            logging.error("Invalid choice. Please enter 'calc', 'history', or 'exit'.")


def command_menu(history_manager, command):
    operations = discover_operations(command.lower())
    while True:
        display_menu(operations, command)
        choice = (
            input("Enter the operation name (or 'back' to return to the main menu): ")
            .lower()
            .strip()
        )
        if choice == "exit":
            logging.info("Exiting...")
            return True
        elif choice == "back":
            return False
        elif choice in operations:
            perform_operation(choice, history_manager)
        else:
            logging.error(
                "Invalid operation. Please select a valid operation or 'back'."
            )


def display_menu(operations, command):
    print(f"\n{command} Menu:")
    c = 1
    for operation in operations:
        if command == "History":
            operation = operation.replace("_", " ")
            print(f"{c}. {operation}")
        else:
            print(f"{c}. {operation}")
        c += 1
    print("0. back")


def perform_operation(operation, history_manager):
    try:
        operation_module = importlib.import_module(
            f"app.plugins.calculator.{operation}"
        )
        operation_func = getattr(operation_module, operation)
        num1 = Decimal(input("Enter first number: "))
        num2 = Decimal(input("Enter second number: "))
        result = operation_func(num1, num2)
        print(f"Result of {operation}({num1}, {num2}) = {result}")
        # Save the operation to history
        operations_dict = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}
        history_manager.add_operation(
            f"{num1} {operations_dict[operation]} {num2}", result
        )
    except (ImportError, AttributeError):
        print(f"Error: Operation '{operation}' not found or invalid")
    except Exception as e:
        print(f"An error occurred: {e}")


def discover_operations(command):
    plugins_dir = f"app/plugins/{command}"
    operations = []
    for item in os.listdir(plugins_dir):
        item_path = os.path.join(plugins_dir, item)
        if os.path.isdir(item_path):
            operations.append(item)
    return operations


def calculate_and_print(num1, num2, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [num1, num2])
        operation_module = importlib.import_module(
            f"app.plugins.calculator.{operation_name}"
        )
        operation_func = getattr(operation_module, operation_name)
        result = operation_func(a_decimal, b_decimal)
        print(f"The result of {num1} {operation_name} {num2} is equal to {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
