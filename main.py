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
    history_manager = HistoryManager(
        os.getenv("HIST_DIREC")
    )  # Create an instance of HistoryManager
    while True:
        display_main_menu()
        choice = input("Enter your choice (calc, history, exit): ").lower().strip()
        if choice == "exit":
            logging.info("Exiting...")
            break
        elif choice == "calc":
            if calculator_menu(history_manager):
                break
        elif choice == "history":
            if history_menu(history_manager):
                break
        else:
            logging.error("Invalid choice. Please enter 'calc', 'history', or 'exit'.")


def display_main_menu():
    print("\nMain Menu:")
    print("1. Calculator")
    print("2. History")
    print("3. Exit")


def calculator_menu(history_manager):
    operations = discover_operations()
    while True:
        display_calculator_menu(operations)
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


def history_menu(history_manager):
    while True:
        display_history_menu()
        choice = input("Enter your choice (1, 2, 3, 4, 5, back): ").lower().strip()
        if choice == "exit":
            logging.info("Exiting...")
            return True
        elif choice == "back":
            return False
        elif choice == "1":
            view_history(history_manager)
        elif choice == "2":
            clear_history(history_manager)
        elif choice == "3":
            delete_record(history_manager)
        elif choice == "4":
            add_operation(history_manager)
        elif choice == "5":
            # Additional history-related functionality
            pass
        else:
            logging.error("Invalid choice. Please enter a valid option.")


def display_calculator_menu(operations):
    print("\nCalculator Menu:")
    for operation in operations:
        print(operation)
    print("back")


def display_history_menu():
    print("\nHistory Menu:")
    print("1. View History")
    print("2. Clear History")
    print("3. Delete Record")
    print("4. Add Operation")
    print("5. Additional History Functionality")
    print("back")


def view_history(history_manager):
    print("\nHistory:")
    print(history_manager.history)


def clear_history(history_manager):
    history_manager.clear_history()
    print("History cleared.")


def delete_record(history_manager):
    index = int(input("Enter the index of the record to delete: "))
    history_manager.delete_record(index)
    print("Record deleted.")


def add_operation(history_manager):
    expression = input("Enter expression: ")
    result = input("Enter result: ")
    history_manager.add_operation(expression, result)
    print("Operation added.")


def perform_operation(operation, history_manager):
    try:
        operation_module = importlib.import_module(f"app.plugins.{operation}")
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


def discover_operations():
    plugins_dir = "app/plugins"
    operations = []
    for item in os.listdir(plugins_dir):
        item_path = os.path.join(plugins_dir, item)
        if os.path.isdir(item_path):
            operations.append(item)
    return operations
def calculate_and_print(num1, num2, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [num1, num2])
        operation_module = importlib.import_module(f"app.plugins.{operation_name}")
        operation_func = getattr(operation_module, operation_name)
        result = operation_func(a_decimal, b_decimal)
        print(f"The result of {num1} {operation_name} {num2} is equal to {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
