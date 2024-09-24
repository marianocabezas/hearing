import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Intervention Type': ['Hearing Test', 'Referral'],
        'Percentage (%)': [36, 64]}


# Create the bar chart
sns.barplot(x='Intervention Type', y='Percentage (%)', data=data)

# Display the plot
plt.savefig('bar_chart.png')