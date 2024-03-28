"""Addition operation."""

import logging
from decimal import Decimal


def add(a: Decimal, b: Decimal) -> Decimal:
    """Perform addition of two Decimal numbers."""
    logging.info(f"Performing addition operation: {a} + {b}")
    result = a + b
    logging.info(f"Addition result: {result}")
    return result
