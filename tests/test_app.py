import pytest
from decimal import Decimal
from calculator import Calculator
from main import calculate_and_print


@pytest.mark.parametrize(
    "a, b, operation, expected",
    [
        (Decimal("2"), Decimal("2"), "add", Decimal("4")),
        (Decimal("2"), Decimal("2"), "subtract", Decimal("0")),
        (Decimal("2"), Decimal("2"), "divide", Decimal("1")),
        (Decimal("2"), Decimal("2"), "multiply", Decimal("4")),
    ],
)
def test_operation(a, b, operation, expected):
    result = Calculator.load_operation(operation)(a, b)
    assert result == expected, f"{operation} operation failed"


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.load_operation("divide")(Decimal("10"), Decimal("0"))


def test_load_invalid_operation():

    with pytest.raises(ValueError):
        Calculator.load_operation("invalid_operation")


def test_load_unknown_operation():

    with pytest.raises(ValueError):
        Calculator.load_operation("unknown_operation")


def test_load_operation_operation_not_found():

    with pytest.raises(ValueError):
        Calculator.load_operation("operation_not_found")


@pytest.mark.parametrize(
    "a, b, operation, expected",
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
            "An error occurred: No module named 'plugin.unknown'",
        ),
        (
            "a",
            Decimal("3"),
            "add",
            "An error occurred: [<class 'decimal.ConversionSyntax'>]",
        ),
        (
            Decimal("7"),
            "b",
            "subtract",
            "An error occurred: [<class 'decimal.ConversionSyntax'>]",
        ),
    ],
)
def test_calculate_and_print(a, b, operation, expected, capsys):
    calculate_and_print(a, b, operation)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
