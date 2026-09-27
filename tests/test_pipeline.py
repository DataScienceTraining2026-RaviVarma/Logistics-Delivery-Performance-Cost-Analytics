import pandas as pd
import pytest
from src.data_cleaner import clean_data, remove_duplicates, create_derived_columns
from src.business_analysis import calculate_total_orders, calculate_on_time_percentage

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'order_id': ['1', '2', '2'],
        'customer_id': ['C1', 'C2', 'C2'],
        'order_date': ['2023-01-01', '2023-01-02', '2023-01-02'],
        'dispatch_date': ['2023-01-02', '2023-01-03', '2023-01-03'],
        'expected_delivery_date': ['2023-01-05', '2023-01-06', '2023-01-06'],
        'actual_delivery_date': ['2023-01-04', '2023-01-08', '2023-01-08'],
        'distance_km': [100, 200, 200],
        'shipping_cost': [50, 100, 100],
        'fuel_cost': [10, 20, 20],
        'quantity': [1, 2, 2],
        'weight_kg': [5, 10, 10],
        'warehouse_processing_hours': [12, 24, 24],
        'delivery_status': ['Delivered', 'Delivered', 'Delivered'],
        'shipping_mode': ['Air', 'Road', 'Road']
    })

def test_load_data():
    # Placeholder for IO test
    assert True

def test_remove_duplicates(sample_data):
    df = remove_duplicates(sample_data)
    assert len(df) == 2

def test_create_derived_columns(sample_data):
    sample_data['actual_delivery_date'] = pd.to_datetime(sample_data['actual_delivery_date'])
    sample_data['dispatch_date'] = pd.to_datetime(sample_data['dispatch_date'])
    sample_data['expected_delivery_date'] = pd.to_datetime(sample_data['expected_delivery_date'])
    
    df = create_derived_columns(sample_data)
    assert 'delivery_days' in df.columns
    assert 'delay_days' in df.columns
    assert df['on_time_flag'].iloc[0] == 1  # Delivered early/on-time
    assert df['on_time_flag'].iloc[1] == 0  # Delayed

def test_calculate_total_orders(sample_data):
    df = remove_duplicates(sample_data)
    assert calculate_total_orders(df) == 2

def test_calculate_on_time_percentage(sample_data):
    sample_data['actual_delivery_date'] = pd.to_datetime(sample_data['actual_delivery_date'])
    sample_data['dispatch_date'] = pd.to_datetime(sample_data['dispatch_date'])
    sample_data['expected_delivery_date'] = pd.to_datetime(sample_data['expected_delivery_date'])
    df = create_derived_columns(remove_duplicates(sample_data))
    assert calculate_on_time_percentage(df) == 50.0

def test_save_cleaned_data():
    # Placeholder for IO test
    assert True