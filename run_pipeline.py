import os
from src.data_loader import load_data
from src.data_cleaner import clean_data, save_cleaned_data

def run_pipeline():
    """Run the complete data cleaning pipeline."""
    raw_path = "data/raw/logistics_data.csv"
    clean_path = "data/cleaned/logistics_cleaned.csv"
    
    print("Loading raw data...")
    df = load_data(raw_path)
    
    if df is not None:
        print("Cleaning data and applying business rules...")
        cleaned_df = clean_data(df)
        
        print("Saving cleaned data...")
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(clean_path), exist_ok=True)
        save_cleaned_data(cleaned_df, clean_path)
        
        print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()