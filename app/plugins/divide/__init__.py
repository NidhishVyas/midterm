"""Division operation."""

import logging
from decimal import Decimal


def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division of two Decimal numbers."""
    logging.info(f"Performing division operation: {a} / {b}")
    if b == 0:
        logging.error("Division by zero error")
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    logging.info(f"Division result: {result}")
    return result
