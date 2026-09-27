import pandas as pd

# Basic KPIs
def calculate_total_orders(df):
    """Return total number of unique orders."""
    return df['order_id'].nunique()

def calculate_total_delivered(df):
    """Return count of delivered orders."""
    return len(df[df['delivery_status'] == 'Delivered'])

def calculate_total_delayed(df):
    """Return count of delayed orders."""
    return len(df[df['delay_days'] > 0])

def calculate_on_time_percentage(df):
    """Return percentage of delivered orders that were on time."""
    delivered = calculate_total_delivered(df)
    if delivered == 0:
        return 0.0
    on_time = len(df[(df['delivery_status'] == 'Delivered') & (df['on_time_flag'] == 1)])
    return (on_time / delivered) * 100

def calculate_average_delivery_days(df):
    """Return overall average delivery days."""
    return df['delivery_days'].mean()

def calculate_average_delay_days(df):
    """Return average delay duration for delayed shipments."""
    return df[df['delay_days'] > 0]['delay_days'].mean()

# Cost KPIs
def calculate_total_shipping_cost(df):
    """Return sum of all shipping costs."""
    return df['shipping_cost'].sum()

def calculate_average_shipping_cost(df):
    """Return average shipping cost per order."""
    return df['shipping_cost'].mean()

def calculate_total_fuel_cost(df):
    """Return total fuel costs."""
    return df['fuel_cost'].sum()

def calculate_total_logistics_cost(df):
    """Return overall logistics cost."""
    return df['total_logistics_cost'].sum()

def calculate_average_logistics_cost(df):
    """Return average total logistics cost."""
    return df['total_logistics_cost'].mean()

def calculate_average_cost_per_km(df):
    """Return average cost per kilometer traveled."""
    return df['cost_per_km'].mean()

# Aggregation Analyses
def analyze_route_performance(df):
    """Return performance aggregated by origin to destination route."""
    return df.groupby(['origin_city', 'destination_city']).agg({'order_id': 'count', 'delivery_days': 'mean'}).reset_index()

def analyze_route_cost(df):
    """Return average cost segmented by route."""
    return df.groupby(['origin_city', 'destination_city'])['total_logistics_cost'].mean().reset_index()

def analyze_route_delays(df):
    """Return average delay days segmented by route."""
    return df.groupby(['origin_city', 'destination_city'])['delay_days'].mean().reset_index()

def analyze_warehouse_performance(df):
    """Return volume handled by each warehouse."""
    return df.groupby('warehouse')['order_id'].count().reset_index()

def analyze_warehouse_delays(df):
    """Return delay performance by warehouse."""
    return df.groupby('warehouse')['delay_days'].mean().reset_index()

def analyze_warehouse_processing_time(df):
    """Return average processing time by warehouse."""
    return df.groupby('warehouse')['warehouse_processing_hours'].mean().reset_index()

def analyze_shipping_mode(df):
    """Return volume by shipping mode."""
    return df.groupby('shipping_mode')['order_id'].count().reset_index()

def analyze_shipping_mode_cost(df):
    """Return costs across shipping modes."""
    return df.groupby('shipping_mode')['total_logistics_cost'].mean().reset_index()

def analyze_shipping_mode_delays(df):
    """Return delay profiles by shipping mode."""
    return df.groupby('shipping_mode')['delay_days'].mean().reset_index()

def analyze_delivery_partner(df):
    """Return volume mapped to delivery partners."""
    return df.groupby('delivery_partner')['order_id'].count().reset_index()

def analyze_partner_cost(df):
    """Return average partner logistics costs."""
    return df.groupby('delivery_partner')['total_logistics_cost'].mean().reset_index()

def analyze_partner_delays(df):
    """Return average partner delay duration."""
    return df.groupby('delivery_partner')['delay_days'].mean().reset_index()

def analyze_partner_damage_rate(df):
    """Return damage percentage rates by delivery partner."""
    df_partner = df.groupby('delivery_partner').agg(total_orders=('order_id', 'count'), damages=('damage_flag', 'sum')).reset_index()
    df_partner['damage_rate'] = (df_partner['damages'] / df_partner['total_orders']) * 100
    return df_partner[['delivery_partner', 'damage_rate']]

# Customer KPIs
def calculate_average_customer_rating(df):
    """Return overall average customer rating."""
    return df['customer_rating'].mean()

def calculate_return_rate(df):
    """Return percentage of total returned orders."""
    return (df['return_flag'].sum() / len(df)) * 100 if len(df) > 0 else 0

def calculate_damage_rate(df):
    """Return percentage of total damaged orders."""
    return (df['damage_flag'].sum() / len(df)) * 100 if len(df) > 0 else 0