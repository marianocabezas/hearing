import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {'Intervention Type': ['Hearing Test', 'Referral'],
        'Percentage (%)': [36, 64]}


df = pd.DataFrame(data)
x_label = 'Intervention Type'
y_label = 'Percentage (%)'
save_file_name = 'chart_styles/bar_chart/bar_chart.png'
title = "Bar chart"

def create_bar_chart(df, x_label, y_label, save_file_name, title=""):
        # Create the bar chart
        sns.barplot(x=x_label, y=y_label, data=df)
        # plt.title(title)
        # Display the plot
        plt.savefig(save_file_name)

if __name__ == "__main__":
        create_bar_chart(df, title, x_label, y_label, save_file_name)