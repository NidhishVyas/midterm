"""Subtraction operation."""

import logging
from decimal import Decimal


def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Perform subtraction of two Decimal numbers."""
    logging.info(f"Performing subtraction operation: {a} - {b}")
    result = a - b
    logging.info(f"Subtraction result: {result}")
    return result
