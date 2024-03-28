from decimal import Decimal
from typing import Callable
import importlib


class Calculator:

    @staticmethod
    def _perform_operation(
        num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ) -> Decimal:
        """Internal method to perform an operation."""
        from app.commands.calculation import Calculation

        calculation = Calculation.create(num1, num2, operation)
        return calculation.perform()

    @staticmethod
    def load_operation(operation_name: str) -> Callable[[Decimal, Decimal], Decimal]:
        """Load an arithmetic operation function dynamically from a plugin."""
        try:
            plugin_module = importlib.import_module(f"app.plugins.{operation_name}")
            operation_func = getattr(plugin_module, operation_name)
            return operation_func
        except (ImportError, AttributeError):
            raise ValueError(f"Operation '{operation_name}' not found or invalid")

    @staticmethod
    def add(num1: Decimal, num2: Decimal) -> Decimal:
        return Calculator._perform_operation(
            num1, num2, Calculator.load_operation("add")
        )

    @staticmethod
    def subtract(num1: Decimal, num2: Decimal) -> Decimal:
        return Calculator._perform_operation(
            num1, num2, Calculator.load_operation("subtract")
        )

    @staticmethod
    def multiply(num1: Decimal, num2: Decimal) -> Decimal:
        return Calculator._perform_operation(
            num1, num2, Calculator.load_operation("multiply")
        )

    @staticmethod
    def divide(num1: Decimal, num2: Decimal) -> Decimal:
        return Calculator._perform_operation(
            num1, num2, Calculator.load_operation("divide")
        )
