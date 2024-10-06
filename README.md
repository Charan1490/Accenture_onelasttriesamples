ESG and Compliance Visualization Scripts
This repository contains three Python scripts designed to generate and visualize compliance audit results and various ESG (Environmental, Social, and Governance) performance metrics for multiple companies. These scripts use random sample data to create meaningful visualizations, which can be adapted to real datasets.

Prerequisites
Before running these scripts, ensure that you have the required libraries installed. You can install them via pip:
pip install matplotlib pandas plotly numpy

1. Audit Results
Description:
This script simulates compliance audit results over a period of 52 weeks, generating random compliance percentages. It highlights violations where compliance falls below a certain threshold.

How to Use:
Simply run the script:
python Audit\ results.py
Output:
A line graph showing compliance percentages over time.
Violations (if any) will be marked in red and annotated.
The graph will be saved as compliance_audit_results.png in your working directory.
The graph will also display on screen with the compliance data.

2. ESG Performance
Description:
This script generates random data for various ESG metrics (Carbon Emissions, Water Usage, Workforce Diversity, and Community Engagement) over a span of years (2018–2024) and plots them using interactive plotly graphs.

How to Use:
Run the script using:

python ESG\ performance.py
Output:
A line chart showing Carbon Emissions over time.
A bar chart representing annual Water Usage.
A pie chart displaying Workforce Diversity.
A line chart representing the Community Engagement score over time.
All graphs are interactive and will be displayed in your browser using plotly.

3. ESG Score Visualization for Multiple Companies
Description:
This script generates ESG scores for five companies over a 20-month period and compares their performance against a calculated benchmark average. The ESG scores simulate gradual changes over time for each company.

How to Use:
Execute the script using:
python Graph.py
Output:
A line graph for each company's ESG score over time.
A benchmark average line to compare each company's performance against the overall trend.
The graph will display on the screen and show how each company’s ESG score evolves compared to the benchmark.

Customization
You can replace the random data generation with your real data by modifying the sections where data is generated for compliance, ESG metrics, and company performance.
