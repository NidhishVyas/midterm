"""Multiplication operation."""

import logging
from decimal import Decimal


def multiply(num1: Decimal, num2: Decimal) -> Decimal:
    """Perform multiplication of two Decimal numbers."""
    logging.info(f"Performing multiplication operation: {num1} * {num2}")
    result = num1 * num2
    logging.info(f"Multiplication result: {result}")
    return result
