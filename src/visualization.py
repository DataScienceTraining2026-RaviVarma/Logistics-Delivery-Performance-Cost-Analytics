import matplotlib.pyplot as plt
import seaborn as sns

def plot_delivery_status(df):
    """Display count of deliveries by status."""
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='delivery_status', ax=ax, palette='viridis')
    ax.set_title('Delivery Status Distribution')
    return fig

def plot_monthly_orders(df):
    """Display order count by month."""
    fig, ax = plt.subplots(figsize=(8, 4))
    df['order_month'] = df['order_date'].dt.to_period('M')
    monthly = df.groupby('order_month')['order_id'].count()
    monthly.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Monthly Order Trend')
    ax.set_ylabel('Order Count')
    return fig

def plot_monthly_delivery_performance(df):
    """Display on-time performance trend by month."""
    fig, ax = plt.subplots(figsize=(8, 4))
    df['month'] = df['actual_delivery_date'].dt.to_period('M')
    perf = df.groupby('month')['on_time_flag'].mean() * 100
    perf.plot(kind='line', marker='o', ax=ax, color='green')
    ax.set_title('Monthly Delivery Performance (%)')
    ax.set_ylabel('On-Time %')
    return fig

def plot_delay_by_warehouse(df):
    """Display average delay grouped by warehouse."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df, x='warehouse', y='delay_days', ax=ax, ci=None)
    ax.set_title('Average Delay by Warehouse')
    return fig

def plot_delay_by_shipping_mode(df):
    """Display delays by shipping mode."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df, x='shipping_mode', y='delay_days', ax=ax, ci=None)
    ax.set_title('Average Delay by Shipping Mode')
    return fig

def plot_delay_by_route(df):
    """Display delays for top 10 routes."""
    fig, ax = plt.subplots(figsize=(10, 5))
    df['route'] = df['origin_city'] + " to " + df['destination_city']
    route_delays = df.groupby('route')['delay_days'].mean().sort_values(ascending=False).head(10)
    route_delays.plot(kind='bar', ax=ax, color='orange')
    ax.set_title('Top 10 Routes with Highest Delay')
    ax.set_ylabel('Avg Delay (Days)')
    return fig

def plot_delay_distribution(df):
    """Display histogram of delay days."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[df['delay_days'] > 0]['delay_days'], bins=20, ax=ax, kde=True, color='red')
    ax.set_title('Delay Distribution (Delayed Orders Only)')
    return fig

def plot_cost_by_shipping_mode(df):
    """Display logistics cost by shipping mode."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(data=df, x='shipping_mode', y='total_logistics_cost', ax=ax)
    ax.set_title('Cost by Shipping Mode')
    return fig

def plot_cost_by_route(df):
    """Display costs for top 10 most expensive routes."""
    fig, ax = plt.subplots(figsize=(10, 5))
    df['route'] = df['origin_city'] + " to " + df['destination_city']
    route_costs = df.groupby('route')['total_logistics_cost'].mean().sort_values(ascending=False).head(10)
    route_costs.plot(kind='bar', ax=ax, color='purple')
    ax.set_title('Top 10 Most Expensive Routes')
    return fig

def plot_cost_trend(df):
    """Display average cost trend over time."""
    fig, ax = plt.subplots(figsize=(8, 4))
    df['order_month'] = df['order_date'].dt.to_period('M')
    cost_trend = df.groupby('order_month')['total_logistics_cost'].mean()
    cost_trend.plot(kind='line', marker='x', ax=ax, color='brown')
    ax.set_title('Average Cost Trend by Month')
    return fig

def plot_orders_by_warehouse(df):
    """Display order counts across warehouses."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(data=df, x='warehouse', ax=ax, palette='mako')
    ax.set_title('Orders by Warehouse')
    return fig

def plot_processing_time_by_warehouse(df):
    """Display warehouse processing hour averages."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df, x='warehouse', y='warehouse_processing_hours', ax=ax, ci=None)
    ax.set_title('Processing Time by Warehouse')
    return fig

def plot_shipments_by_partner(df):
    """Display total shipments managed by each delivery partner."""
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.countplot(data=df, x='delivery_partner', ax=ax, palette='cubehelix')
    ax.set_title('Shipments by Delivery Partner')
    plt.xticks(rotation=45)
    return fig

def plot_partner_delivery_performance(df):
    """Display partner performance."""
    fig, ax = plt.subplots(figsize=(10, 4))
    partner_perf = df.groupby('delivery_partner')['on_time_flag'].mean().sort_values() * 100
    partner_perf.plot(kind='bar', ax=ax, color='teal')
    ax.set_title('On-Time Delivery % by Partner')
    ax.set_ylabel('% On Time')
    return fig

def plot_partner_cost(df):
    """Display cost averages by partner."""
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(data=df, x='delivery_partner', y='total_logistics_cost', ax=ax, ci=None)
    ax.set_title('Average Cost by Partner')
    plt.xticks(rotation=45)
    return fig

def plot_customer_rating_distribution(df):
    """Display histogram of customer ratings."""
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['customer_rating'].dropna(), bins=5, ax=ax, color='gold')
    ax.set_title('Customer Rating Distribution')
    return fig

def plot_rating_by_delivery_status(df):
    """Display customer rating averages by delivery status."""
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df, x='delivery_status', y='customer_rating', ax=ax, ci=None, palette='pastel')
    ax.set_title('Rating by Delivery Status')
    return fig