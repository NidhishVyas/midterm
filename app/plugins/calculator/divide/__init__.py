"""Division operation."""

import logging
from decimal import Decimal


def divide(num1: Decimal, num2: Decimal) -> Decimal:
    """Perform division of two Decimal numbers."""
    logging.info(f"Performing division operation: {num1} / {num2}")
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = num1 / num2
    logging.info(f"Division result: {result}")
    return result
