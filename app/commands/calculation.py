from decimal import Decimal
from typing import Callable
from app.commands import Calculator


class Calculation:
    """Represents a calculation operation between two Decimal numbers."""

    def __init__(
        self,
        num1: Decimal,
        num2: Decimal,
        operation: Callable[[Decimal, Decimal], Decimal],
    ):
        """Initialize a Calculation object."""
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    @staticmethod
    def create(num1: Decimal, num2: Decimal, operation_name: str) -> "Calculation":
        """Factory method to create a Calculation object with a specified operation."""
        operation = Calculator.load_operation(operation_name)
        return Calculation(num1, num2, operation)

    def __repr__(self) -> str:
        """Return a string representation of the Calculation object."""
        return f"Calculation({self.num1}, {self.num2}, {self.operation.__name__})"

    def perform(self) -> Decimal:
        """Perform the calculation operation and return the result."""
        return self.operation(self.num1, self.num2)
