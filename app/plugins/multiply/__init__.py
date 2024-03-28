"""Multiplication operation."""

import logging
from decimal import Decimal


def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Perform multiplication of two Decimal numbers."""
    logging.info(f"Performing multiplication operation: {a} * {b}")
    result = a * b
    logging.info(f"Multiplication result: {result}")
    return result
