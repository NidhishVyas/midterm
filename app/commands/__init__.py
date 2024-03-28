# calculator.py
from decimal import Decimal
import importlib
from typing import Callable


class Calculation:
    """Represents a calculation operation between two Decimal numbers."""

    @staticmethod
    def load_operation(operation_name: str) -> Callable[[Decimal, Decimal], Decimal]:
        """Load an arithmetic operation function dynamically from a plugin."""
        try:
            plugin_module = importlib.import_module(f"app.plugins.{operation_name}")
            operation_func = getattr(plugin_module, operation_name)
            return operation_func
        except (ImportError, AttributeError):
            raise ValueError(f"Operation '{operation_name}' not found or invalid")


# class CalculatorREPL(cmd.Cmd):
#     def __init__(self):
#         super().__init__()
#         self.history_manager = None  # Initialize history_manager as None

#     def set_history_manager(self, history_manager):
#         self.history_manager = history_manager  # Set the history manager

#     # Add methods to interact with history_manager
#     def do_load_history(self, arg):
#         """Load history records."""
#         if self.history_manager:
#             # Call methods of history_manager
#             self.history_manager.load_history()
#         else:
#             print("History manager not set.")

#     def do_save_history(self, arg):
#         """Save history records."""
#         if self.history_manager:
#             self.history_manager.save_history()
#         else:
#             print("History manager not set.")

#     def do_clear_history(self, arg):
#         """Clear history records."""
#         if self.history_manager:
#             self.history_manager.clear_history()
#         else:
#             print("History manager not set.")

#     def do_delete_record(self, arg):
#         """Delete a history record."""
#         if self.history_manager:
#             try:
#                 index = int(arg)
#                 self.history_manager.delete_record(index)
#             except ValueError:
#                 print("Invalid index.")
#         else:
#             print("History manager not set.")
