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
