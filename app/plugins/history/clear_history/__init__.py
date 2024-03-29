import pandas as pd


def clear_history(history_file):
    """Clears all entries from the history."""
    # Clear history DataFrame
    history_df = pd.DataFrame(columns=["Operation", "Result"])

    # Save the cleared DataFrame back to the file
    history_df.to_csv(history_file, index=True)

    print("History has been cleared.")
