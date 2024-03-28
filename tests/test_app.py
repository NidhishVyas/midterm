"""Test module for calculator."""

from decimal import Decimal
import pytest
from app.commands import Calculator
from main import calculate_and_print


@pytest.mark.parametrize(
    "num1, num2, operation, expected",
    [
        (Decimal("2"), Decimal("2"), "add", Decimal("4")),
        (Decimal("2"), Decimal("2"), "subtract", Decimal("0")),
        (Decimal("2"), Decimal("2"), "divide", Decimal("1")),
        (Decimal("2"), Decimal("2"), "multiply", Decimal("4")),
    ],
)
def test_operation(num1, num2, operation, expected):
    """
    Test basic arithmetic operations.

    Parameters:
        num1 (Decimal): The first operand.
        num2 (Decimal): The second operand.
        operation (str): The operation to perform.
        expected (Decimal): The expected result.
    """
    result = Calculator.load_operation(operation)(num1, num2)
    assert result == expected, f"{operation} operation failed"


def test_divide_by_zero():
    """
    Test division by zero.

    Raises:
        ZeroDivisionError: If division by zero occurs.
    """
    with pytest.raises(ZeroDivisionError):
        Calculator.load_operation("divide")(Decimal("10"), Decimal("0"))


def test_load_invalid_operation():
    """
    Test loading an invalid operation.

    Raises:
        ValueError: If an invalid operation is loaded.
    """
    with pytest.raises(ValueError):
        Calculator.load_operation("invalid_operation")


def test_load_unknown_operation():
    """
    Test loading an unknown operation.

    Raises:
        ValueError: If an unknown operation is loaded.
    """
    with pytest.raises(ValueError):
        Calculator.load_operation("unknown_operation")


def test_load_operation_operation_not_found():
    """
    Test loading an operation that is not found.

    Raises:
        ValueError: If the operation is not found.
    """
    with pytest.raises(ValueError):
        Calculator.load_operation("operation_not_found")


@pytest.mark.parametrize(
    "num1, num2, operation, expected",
    [
        (
            Decimal("4"),
            Decimal("4"),
            "divide",
            "The result of 4 divide 4 is equal to 1",
        ),
        (
            Decimal("5"),
            Decimal("5"),
            "unknown",
            "An error occurred: No module named 'app.plugins.unknown'",
        ),
        (
            "num1",
            Decimal("3"),
            "add",
            "An error occurred: [<class 'decimal.ConversionSyntax'>]",
        ),
        (
            Decimal("7"),
            "num2",
            "subtract",
            "An error occurred: [<class 'decimal.ConversionSyntax'>]",
        ),
    ],
)
def test_calculate_and_print(num1, num2, operation, expected, capsys):
    """
    Test the calculate_and_print function with various inputs.

    Parameters:
        num1 (Decimal or str): The first operand.
        num2 (Decimal or str): The second operand.
        operation (str): The operation to perform.
        expected (str): The expected output message.
        capsys: pytest fixture for capturing stdout/stderr.
    """
    calculate_and_print(num1, num2, operation)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
