
import sys
import os

# Add the root directory to the Python path so the 'src' module is recognized
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.business_analysis import *
from src.visualization import *



def load_dashboard_data():
    """Load cleaned dataset into Streamlit."""
    return pd.read_csv("data/cleaned/logistics_cleaned.csv", parse_dates=['order_date', 'dispatch_date', 'expected_delivery_date', 'actual_delivery_date'])

def show_sidebar_filters(df):
    """Provide dashboard filter widgets."""
    st.sidebar.header("Data Filters")
    warehouse = st.sidebar.multiselect("Warehouse", options=df['warehouse'].unique(), default=df['warehouse'].unique())
    mode = st.sidebar.multiselect("Shipping Mode", options=df['shipping_mode'].unique(), default=df['shipping_mode'].unique())
    partner = st.sidebar.multiselect("Delivery Partner", options=df['delivery_partner'].unique(), default=df['delivery_partner'].unique())
    
    # Apply user filters
    filtered_df = df[df['warehouse'].isin(warehouse) & df['shipping_mode'].isin(mode) & df['delivery_partner'].isin(partner)]
    return filtered_df

def show_overview(df):
    """Display Page 1 - Executive Overview KPIs."""
    st.header("Executive Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", calculate_total_orders(df))
    col2.metric("Delivered Orders", calculate_total_delivered(df))
    col3.metric("Delayed Orders", calculate_total_delayed(df))
    
    col4, col5, col6 = st.columns(3)
    col4.metric("On-Time %", f"{calculate_on_time_percentage(df):.2f}%")
    col5.metric("Avg Delivery Days", f"{calculate_average_delivery_days(df):.2f}")
    col6.metric("Total Logistics Cost", f"${calculate_total_logistics_cost(df):,.2f}")

def show_delivery_analysis(df):
    """Display Page 2 - Delivery Analysis."""
    st.header("Delivery Analysis")
    st.pyplot(plot_delivery_status(df))
    st.pyplot(plot_monthly_delivery_performance(df))
    st.pyplot(plot_delay_distribution(df))

def show_route_analysis(df):
    """Display Page 3 - Route Analysis."""
    st.header("Route Analysis")
    st.pyplot(plot_delay_by_route(df))
    st.pyplot(plot_cost_by_route(df))

def show_warehouse_analysis(df):
    """Display Page 4 - Warehouse Analysis."""
    st.header("Warehouse Analysis")
    st.pyplot(plot_orders_by_warehouse(df))
    st.pyplot(plot_processing_time_by_warehouse(df))
    st.pyplot(plot_delay_by_warehouse(df))

def show_cost_analysis(df):
    """Display Page 5 - Cost Analysis."""
    st.header("Cost Analysis")
    col1, col2 = st.columns(2)
    col1.metric("Total Cost", f"${calculate_total_logistics_cost(df):,.2f}")
    col2.metric("Avg Cost / Order", f"${calculate_average_logistics_cost(df):.2f}")
    st.pyplot(plot_cost_by_shipping_mode(df))
    st.pyplot(plot_cost_trend(df))

def show_partner_analysis(df):
    """Display Page 6 - Partner Analysis."""
    st.header("Partner Analysis")
    st.pyplot(plot_shipments_by_partner(df))
    st.pyplot(plot_partner_delivery_performance(df))
    st.pyplot(plot_partner_cost(df))

def main():
    """Main Streamlit application flow."""
    st.set_page_config(page_title="Logistics Dashboard", layout="wide")
    st.title("Logistics Delivery Performance & Cost Analytics")
    
    try:
        df = load_dashboard_data()
    except FileNotFoundError:
        st.error("Cleaned data not found. Please run 'run_pipeline.py' first.")
        return

    filtered_df = show_sidebar_filters(df)
    
    pages = {
        "Executive Overview": show_overview,
        "Delivery Analysis": show_delivery_analysis,
        "Route Analysis": show_route_analysis,
        "Warehouse Analysis": show_warehouse_analysis,
        "Cost Analysis": show_cost_analysis,
        "Partner Analysis": show_partner_analysis
    }
    
    selection = st.sidebar.radio("Navigate Pages", list(pages.keys()))
    pages[selection](filtered_df)

if __name__ == "__main__":
    main()