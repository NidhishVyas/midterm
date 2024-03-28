import os
import pkgutil
import importlib
import sys
from decimal import Decimal


def main():
    operations = discover_operations()
    while True:
        display_menu(operations)
        choice = input("Enter the operation name (or 'exit' to quit): ")
        if choice.lower() == "exit":
            break
        elif choice in operations:
            print("here")
            perform_operation(choice)


def load_environment_variables(self):
    settings = {key: value for key, value in os.environ.items()}
    return settings


def get_environment_variable(self, env_var: str = "ENVIRONMENT"):
    return self.settings.get(env_var, None)


def load_plugins(self):
    plugins_package = "app.plugins"
    plugins_path = plugins_package.replace(".", "/")
    for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
        if is_pkg:
            try:
                plugin_module = importlib.import_module(
                    f"{plugins_package}.{plugin_name}"
                )
                self.register_plugin_commands(plugin_module, plugin_name)
            except ImportError as e:
                print(f"Error importing plugins {plugin_name}: {e}")


def register_plugin_commands(self, plugin_module, plugin_name):
    for item_name in dir(plugin_module):
        item = getattr(plugin_module, item_name)
        if isinstance(item, type):
            self.command_handler.register_command(plugin_name, item())


def start(self):
    self.load_plugins()
    try:
        while True:
            cmd_input = input(">>> ").strip()
            if cmd_input.lower() == "exit":
                sys.exit(0)
            try:
                self.command_handler.execute_command(cmd_input)
            except KeyError:
                print(f"Unknown command: {cmd_input}")
                sys.exit(1)
    except KeyboardInterrupt:
        print("Application interrupted and exiting gracefully.")
        sys.exit(0)
    finally:
        print("Application shutdown.")


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


def perform_operation(operation):
    try:
        print(operation)
        operation_module = importlib.import_module(f"app.plugins.{operation}")
        operation_func = getattr(operation_module, operation)
        a = Decimal(input("Enter first number: "))
        b = Decimal(input("Enter second number: "))
        result = operation_func(a, b)
        print(f"Result of {operation}({a}, {b}) = {result}")
    except (ImportError, AttributeError) as e:
        print(e)
        print(f"Error: Operation '{operation}' not found or invalid")
    except Exception as e:
        print(f"An error occurred: {e}")


def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        operation_module = importlib.import_module(f"plugins.{operation_name}")
        operation_func = getattr(operation_module, operation_name)
        result = operation_func(a_decimal, b_decimal)
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
