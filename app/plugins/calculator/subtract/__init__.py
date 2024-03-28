"""Subtraction operation."""

import logging
from decimal import Decimal


def subtract(num1: Decimal, num2: Decimal) -> Decimal:
    """Perform subtraction of two Decimal numbers."""
    logging.info(f"Performing subtraction operation: {num1} - {num2}")
    result = num1 - num2
    logging.info(f"Subtraction result: {result}")
    return result
