import os
import pandas as pd

def check_file_exists(file_path):
    """Check if the specified file path exists."""
    return os.path.exists(file_path)

def load_data(file_path):
    """Load CSV data into a Pandas DataFrame."""
    if not check_file_exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    return pd.read_csv(file_path)