import logging
import pandas as pd


def delete_history(history_file, history_manager):
    """Deletes a specific record from the history based on the index."""
    try:
        # Load the history directly from the file for verification
        history_df = pd.read_csv(history_file)

        # Get the index of the entry to delete from user input
        index = int(input("Enter the index of the entry to delete (starting from 0): "))

        # Check if the provided index exists in the DataFrame
        if index in history_df.index:
            # Perform the deletion on the loaded DataFrame
            updated_df = history_df.drop(index)
            updated_df.reset_index(drop=True, inplace=True)

            # Save the updated DataFrame back to the file
            updated_df.to_csv(history_file, index=False)
            logging.info(f"Entry at index {index} has been deleted from the history.")
            print(f"Entry at index {index} has been deleted from the history.")
        else:
            logging.info("Invalid index. Please enter a valid integer that's in range.")
            print("Index was out of bound.")

    except Exception as e:
        # General exception handling
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
