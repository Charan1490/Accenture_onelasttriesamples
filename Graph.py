import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# Generate sample data
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
industries = ['Tech', 'Energy', 'Finance', 'Healthcare', 'Manufacturing']
time_periods = 20
dates = pd.date_range(start='2024-01-01', periods=time_periods, freq='M')

# Create DataFrame
data = []
for company, industry in zip(companies, industries):
    base_score = random.uniform(50, 80)
    scores = [max(0, min(100, base_score + random.uniform(-5, 5) + i*0.5)) for i in range(time_periods)]
    data.extend([(date, company, industry, score) for date, score in zip(dates, scores)])

df = pd.DataFrame(data, columns=['Date', 'Company', 'Industry', 'ESG Score'])

# Calculate benchmark average
benchmark_avg = df.groupby('Date')['ESG Score'].mean()

# Create the plot
plt.figure(figsize=(14, 8))

# Plot each company's ESG score
for company in companies:
    company_data = df[df['Company'] == company]
    plt.plot(company_data['Date'], company_data['ESG Score'], label=f"{company} ({company_data['Industry'].iloc[0]})")

# Plot benchmark average
plt.plot(dates, benchmark_avg, label='Benchmark Average', color='black', linestyle='--', linewidth=2)

# Add labels for key benchmark moments (improvements or worsenings)
for company in companies:
    company_data = df[df['Company'] == company]
    for i in range(1, len(company_data)):
        if abs(company_data['ESG Score'].iloc[i] - company_data['ESG Score'].iloc[i-1]) > 5:
            plt.annotate(f"{company} {'improved' if company_data['ESG Score'].iloc[i] > company_data['ESG Score'].iloc[i-1] else 'worsened'}",
                         (company_data['Date'].iloc[i], company_data['ESG Score'].iloc[i]),
                         xytext=(5, 5), textcoords='offset points', fontsize=8, alpha=0.7)

# Customize the plot
plt.title('ESG Performance Comparison Across Companies')
plt.xlabel('Time')
plt.ylabel('ESG Score')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)

# Add benchmark average box
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = f'Benchmark Average: {benchmark_avg.mean():.2f}'
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('esg_performance_comparison.png')
plt.show()

print("ESG performance comparison graph created and saved as 'esg_performance_comparison.png'")