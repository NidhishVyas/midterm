"""Addition operation."""

import logging
from decimal import Decimal


def add(num1: Decimal, num2: Decimal) -> Decimal:
    """Perform addition of two Decimal numbers."""
    logging.info(f"Performing addition operation: {num1} + {num2}")
    result = num1 + num2
    logging.info(f"Addition result: {result}")
    return result
