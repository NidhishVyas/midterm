"""Division operation."""

from decimal import Decimal


def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division of two Decimal numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    return result
