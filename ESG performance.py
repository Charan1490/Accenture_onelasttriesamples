import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import random

# Generate sample data
years = list(range(2018, 2024))
carbon_emissions = [random.randint(80, 120) for _ in range(len(years))]
water_usage = [random.randint(500, 800) for _ in range(len(years))]
diversity_score = [random.randint(60, 90) for _ in range(len(years))]
community_engagement = [random.randint(70, 95) for _ in range(len(years))]

# Carbon Emissions Line Chart
fig_carbon = go.Figure(data=go.Scatter(x=years, y=carbon_emissions, mode='lines+markers'))
fig_carbon.update_layout(title='Carbon Emissions Over Time', xaxis_title='Year', yaxis_title='CO2 Emissions (tons)')

# Water Usage Bar Chart
fig_water = go.Figure(data=go.Bar(x=years, y=water_usage))
fig_water.update_layout(title='Annual Water Usage', xaxis_title='Year', yaxis_title='Water Usage (m³)')

# Diversity Metrics Pie Chart
diversity_labels = ['Male', 'Female', 'Non-binary', 'Other']
diversity_values = [45, 40, 10, 5]
fig_diversity = go.Figure(data=go.Pie(labels=diversity_labels, values=diversity_values))
fig_diversity.update_layout(title='Workforce Diversity')

# Community Engagement Line Chart
fig_community = go.Figure(data=go.Scatter(x=years, y=community_engagement, mode='lines+markers'))
fig_community.update_layout(title='Community Engagement Score', xaxis_title='Year', yaxis_title='Engagement Score')

# Progress Indicator
current_progress = 75
fig_progress = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = current_progress,

    gauge = {'axis': {'range': [None, 100]},
             'bar': {'color': "darkgreen"},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 80], 'color': "gray"},
                 {'range': [80, 100], 'color': "darkgray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))

# Color-coded Map
countries = ['United States', 'Canada', 'Brazil', 'France', 'Germany', 'China', 'India', 'Australia']
esg_scores = [random.randint(50, 100) for _ in range(len(countries))]

fig_map = px.choropleth(
    locations=countries, 
    locationmode="country names",
    color=esg_scores,
    hover_name=countries,
    color_continuous_scale="Viridis",
    title="Global ESG Performance"
)

# Combine all charts into a dashboard
dashboard = make_subplots(
    rows=3, cols=3,
    specs=[
        [{"type": "scatter"}, {"type": "bar"}, {"type": "indicator"}],
        [{"type": "pie"}, {"type": "scatter"}, {"type": "choropleth"}],
        [{"type": "choropleth"}, None, None]
    ],
    subplot_titles=("Carbon Emissions", "Water Usage", "ESG Target Progress",
                    "Workforce Diversity", "Community Engagement", "Global ESG Performance")
)

dashboard.add_trace(fig_carbon.data[0], row=1, col=1)
dashboard.add_trace(fig_water.data[0], row=1, col=2)
dashboard.add_trace(fig_progress.data[0], row=1, col=3)
dashboard.add_trace(fig_diversity.data[0], row=2, col=1)
dashboard.add_trace(fig_community.data[0], row=2, col=2)
dashboard.add_trace(fig_map.data[0], row=2, col=3)

dashboard.update_layout(height=1000, width=1200, title_text="ESG Performance Dashboard")

# Save the dashboard to an HTML file
dashboard.write_html("esg_dashboard.html")

print("ESG dashboard created and saved as 'esg_dashboard.html'")