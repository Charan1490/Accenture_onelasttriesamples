import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# Generate sample data
dates = pd.date_range(start='2024-01-01', periods=52, freq='W')
compliance_percentages = [random.uniform(80, 100) for _ in range(len(dates))]

# Introduce some alerts (violations)
alert_indices = random.sample(range(len(dates)), 5)
alerts = [compliance_percentages[i] - random.uniform(5, 10) for i in alert_indices]

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Compliance': compliance_percentages})

# Plot the line graph
plt.figure(figsize=(14, 8))
plt.plot(df['Date'], df['Compliance'], label='Compliance Percentage', marker='o')

# Highlight alerts
plt.scatter(df['Date'].iloc[alert_indices], alerts, color='red', zorder=5, label='Alerts')

# Annotate alerts
for i, idx in enumerate(alert_indices):
    plt.annotate(f'Violation {i+1}', (df['Date'].iloc[idx], alerts[i]),
                 textcoords="offset points", xytext=(-15,10), ha='center',
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

# Add labels and title
plt.xlabel('Time (Weeks)')
plt.ylabel('Compliance Percentage')
plt.title('Real-Time Compliance Audit Results')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('compliance_audit_results.png')
plt.show()

print("Compliance audit results graph created and saved as 'compliance_audit_results.png'")