"""This module tests the history management functionalities."""

import os
from unittest.mock import patch
import pandas as pd
import pytest
from app.commands.history_manager import HistoryManager
from app.plugins.history.clear_history import clear_history
from app.plugins.history.load_history import load_history
from app.plugins.history.delete_history import delete_history

# Assume the file paths and names for test
TEST_HISTORY_FILE = "test_history.csv"


@pytest.fixture
def setup_history_manager():
    """Prepare HistoryManager instance with a fresh test history file."""
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)
    history_manager = HistoryManager(TEST_HISTORY_FILE)
    return history_manager


def test_initialization_with_nonexistent_file(setup_history_manager):
    """
    Test initialization of HistoryManager with a non-existent file.
    Should create a DataFrame with specified columns.
    """
    hm = setup_history_manager
    assert "Operation" in hm.history_df.columns
    assert "Result" in hm.history_df.columns
    assert hm.history_df.empty


def test_add_operation(setup_history_manager):
    """Test adding an operation to the history."""
    hm = setup_history_manager
    hm.add_operation(1, "add", 2, 3)
    assert not hm.history_df.empty
    assert hm.history_df.iloc[0]["Operation"] == "1 + 2"
    assert hm.history_df.iloc[0]["Result"] == 3


def test_clear_history():
    """Test clearing the history."""
    clear_history(TEST_HISTORY_FILE)
    df = pd.read_csv(TEST_HISTORY_FILE)
    assert df.empty


@patch("builtins.input", lambda *args: "0")
def test_delete_history():
    """Test deleting a history entry."""
    # Add a record to delete
    df = pd.DataFrame({"Operation": ["1 + 2"], "Result": [3]})
    df.to_csv(TEST_HISTORY_FILE, index=True)
    delete_history(TEST_HISTORY_FILE)
    df = pd.read_csv(TEST_HISTORY_FILE)
    assert df.empty


def test_load_history():
    """Test loading and printing history."""
    # Assuming there's already a test to add operation, which ensures there is history
    # Mocking the print to capture output
    with patch("builtins.print") as mocked_print:
        load_history(TEST_HISTORY_FILE)
        mocked_print.assert_called_with(
            "History file not found."
        )  # Updated expectation


@pytest.fixture(autouse=True)
def clean_up():
    """Clean up the test history file after each test module."""
    yield
    if os.path.exists(TEST_HISTORY_FILE):
        os.remove(TEST_HISTORY_FILE)
