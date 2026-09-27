# Logistics Delivery Performance & Cost Analytics Report

## 1. Executive Summary
This project analyzes the logistics operational data to uncover delivery performance bottlenecks, cost inefficiencies, and route performance, delivering an interactive dashboard for stakeholder use.

## 2. Business Problem
The logistics management team lacked visibility regarding shipment delays, route efficiencies, transportation costs, and partner performance, hampering data-driven decision-making.

## 3. Data Summary
The dataset contained raw customer orders, spanning geographical routing, timestamps, shipping modes, costs, and warehouse information. 

## 4. Data Quality & 5. Cleaning Performed
Initial data profiling revealed missing customer IDs, incorrect date formats, and negative numerical values. The standard cleaning pipeline dropped null critical identifiers, standardized text/dates, applied business validation rules (ensuring non-negative costs and logical dispatch dates), and generated missing derived features like `delay_days` and `total_logistics_cost`.

## 6. KPI Summary
- **On-Time Delivery %:** Calculated to benchmark overarching delivery health.
- **Average Delay Days:** Measured for lagging shipments.
- **Average Logistics Cost:** Tracked per order to ensure margin safety.

## 7. Key Findings
- **Warehouse Bottlenecks:** Specific warehouses correlate strongly with missed dispatch windows.
- **Route Costs:** Long-haul air routes drastically skew total logistics costs compared to localized road networks.
- **Partner Discrepancies:** On-time percentages vary widely depending on the third-party delivery partner assigned.

## 8. Business Recommendations
- **Investigate High-Delay Warehouses:** Operations management must conduct workload analyses on warehouses identified as primary delay sources.
- **Optimize Shipping Modes:** Shift non-urgent deliveries from high-cost Air transport to lower-cost road networks where feasible.
- **Partner Reviews:** Renegotiate contracts or shift volume away from delivery partners with above-average damage and delay rates.

## 9. Conclusion
By applying a rigorous data cleaning pipeline and calculating targeted KPIs, the business now has a clear line-of-sight into operational inefficiencies. Ongoing use of the interactive Streamlit dashboard will allow operations managers to monitor these KPIs continuously and enact proactive routing adjustments.