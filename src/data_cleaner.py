import pandas as pd
import numpy as np

def handle_missing_values(df):
    """Handle missing values according to business rules."""
    df['destination_city'] = df['destination_city'].fillna('Unknown')
    df['shipping_cost'] = df['shipping_cost'].fillna(df['shipping_cost'].median())
    df['fuel_cost'] = df['fuel_cost'].fillna(df['fuel_cost'].median())
    df['warehouse_processing_hours'] = df['warehouse_processing_hours'].fillna(df['warehouse_processing_hours'].median())
    df['customer_rating'] = df['customer_rating'].fillna(df['customer_rating'].median())
    return df

def remove_duplicates(df):
    """Remove duplicate records from the logistics DataFrame."""
    return df.drop_duplicates()

def clean_text_columns(df):
    """Standardize text formatting for categorical columns."""
    text_cols = ['warehouse', 'origin_city', 'destination_city', 'product_category', 'shipping_mode', 'delivery_partner', 'delivery_status']
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.title()
    
    # Convert string flags to numerical flags
    if df['damage_flag'].dtype == 'object':
        df['damage_flag'] = df['damage_flag'].map({'Yes': 1, 'No': 0, '1': 1, '0': 0}).fillna(0).astype(int)
    if df['return_flag'].dtype == 'object':
        df['return_flag'] = df['return_flag'].map({'Yes': 1, 'No': 0, '1': 1, '0': 0}).fillna(0).astype(int)
    return df

def clean_date_columns(df):
    """Convert string date columns to datetime objects."""
    date_cols = ['order_date', 'dispatch_date', 'expected_delivery_date', 'actual_delivery_date']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

def validate_numeric_columns(df):
    """Ensure numeric types for calculation columns."""
    numeric_cols = ['distance_km', 'quantity', 'weight_kg', 'shipping_cost', 'fuel_cost', 'warehouse_processing_hours', 'customer_rating']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def validate_business_rules(df):
    """Apply business validation rules and filter out logically invalid rows."""
    df = df[df['distance_km'] >= 0]
    df = df[df['quantity'] > 0]
    df = df[df['weight_kg'] >= 0]
    df = df[df['shipping_cost'] >= 0]
    df = df[df['fuel_cost'] >= 0]
    df = df[(df['customer_rating'] >= 1) & (df['customer_rating'] <= 5)]
    return df

def create_derived_columns(df):
    """Create new calculated columns based on BRD specifications."""
    df['delivery_days'] = (df['actual_delivery_date'] - df['dispatch_date']).dt.days
    df['delay_days'] = (df['actual_delivery_date'] - df['expected_delivery_date']).dt.days
    
    # Handle cost per km logic safely (avoiding zero division errors)
    df['cost_per_km'] = np.where(df['distance_km'] > 0, df['shipping_cost'] / df['distance_km'], 0.0)
    df['total_logistics_cost'] = df['shipping_cost'] + df['fuel_cost']
    df['on_time_flag'] = np.where(df['delay_days'] <= 0, 1, 0)
    return df

def clean_data(df):
    """Run the master cleaning sequence."""
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = clean_text_columns(df)
    df = clean_date_columns(df)
    df = validate_numeric_columns(df)
    df = validate_business_rules(df)
    df = create_derived_columns(df)
    return df

def save_cleaned_data(df, output_path):
    """Save the fully cleaned DataFrame to a CSV."""
    df.to_csv(output_path, index=False)