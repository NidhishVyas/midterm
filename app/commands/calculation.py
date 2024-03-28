from decimal import Decimal
from typing import Callable
from app.commands import Calculator


class Calculation:
    """Represents a calculation operation between two Decimal numbers."""

    def __init__(
        self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ):
        """Initialize a Calculation object."""
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation_name: str) -> "Calculation":
        """Factory method to create a Calculation object with a specified operation."""
        operation = Calculator.load_operation(operation_name)
        return Calculation(a, b, operation)

    def __repr__(self) -> str:
        """Return a string representation of the Calculation object."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"

    def perform(self) -> Decimal:
        """Perform the calculation operation and return the result."""
        return self.operation(self.a, self.b)
