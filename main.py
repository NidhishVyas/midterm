import os
import pkgutil
import importlib
import sys
from decimal import Decimal
from dotenv import load_dotenv
import logging
import logging.config


def __init__(self):
    os.makedirs("logs", exist_ok=True)
    self.configure_logging()
    load_dotenv()
    self.settings = self.load_environment_variables()
    self.settings.setdefault("ENVIRONMENT", "PRODUCTION")


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
    operations = discover_operations()
    while True:
        display_menu(operations)
        choice = input("Enter the operation name (or 'exit' to quit): ").lower().strip()
        if choice == "exit":
            logging.info("Exiting...")
            break
        elif choice in operations:
            perform_operation(choice)
        else:
            logging.error(
                "Invalid operation name. Please select a valid operation or 'exit'."
            )


def load_environment_variables():
    settings = {key: value for key, value in os.environ.items()}
    logging.info("Environment variables loaded.")
    return settings


def get_environment_variable(self, env_var: str = "ENVIRONMENT"):
    return self.settings.get(env_var, None)


def load_plugins(self):
    plugins_package = "app.plugins"
    plugins_path = plugins_package.replace(".", "/")
    if not os.path.exists(plugins_path):
        logging.warning(f"Plugins directory '{plugins_path}' not found.")
        return
    for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
        if is_pkg:
            try:
                plugin_module = importlib.import_module(
                    f"{plugins_package}.{plugin_name}"
                )
                self.register_plugin_commands(plugin_module, plugin_name)
            except ImportError as e:
                logging.error(f"Error importing plugin {plugin_name}: {e}")


def register_plugin_commands(self, plugin_module, plugin_name):
    for item_name in dir(plugin_module):
        item = getattr(plugin_module, item_name)
        if isinstance(item, type):
            self.command_handler.register_command(plugin_name, item())
            logging.info(
                f"Command '{plugin_name}' from plugin '{plugin_name}' registered."
            )


def discover_operations():
    plugins_dir = "app/plugins"

    operations = []

    for item in os.listdir(plugins_dir):
        item_path = os.path.join(plugins_dir, item)

        if os.path.isdir(item_path):
            operations.append(item)

    return operations


def display_menu(operations):
    print("\nAvailable operations:")
    for operation in operations:
        print(operation)
    print("exit")


def perform_operation(operation):
    try:
        operation_module = importlib.import_module(f"app.plugins.{operation}")
        operation_func = getattr(operation_module, operation)
        num1 = Decimal(input("Enter first number: "))
        num2 = Decimal(input("Enter second number: "))
        result = operation_func(num1, num2)
        print(f"Result of {operation}({num1}, {num2}) = {result}")
    except (ImportError, AttributeError):
        print(f"Error: Operation '{operation}' not found or invalid")
    except Exception as e:
        print(f"An error occurred: {e}")


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
