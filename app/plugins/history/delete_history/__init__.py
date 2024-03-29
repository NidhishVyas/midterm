import pandas as pd

def delete_history(history_file):
    """
    Deletes a specific record from the history based on the index.

    Parameters:
    - history_file (str): The path to the history file (CSV).
    """
    try:
        history_df = pd.read_csv(history_file)
        
        index = int(input("Enter the index of the entry to delete (starting from 0): "))
        
        if index < 0 or index >= len(history_df):
            print("Invalid index. Please enter a valid integer within the range.")
            return
        
        history_df.drop(index, inplace=True)
        history_df.to_csv(history_file, index=True)  # Write back to the CSV file
        
        print(f"Entry at index {index} has been deleted from the history.")
    except ValueError:
        print("Invalid index. Please enter a valid integer.")
    except IndexError:
        print(f"No entry found at the specified index.")
