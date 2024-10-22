import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



save_file_name = 'chart_styles/box_plot/box_plot.png'

# Sample data
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Values': [1, 2, 5, 3, 4, 6, 2, 3, 8]
}

# Create a DataFrame
df = pd.DataFrame(data)
title = 'Box Plot of Values by Category'
x_label = 'Category'
y_label = 'Values'

def create_box_plot(df, title, x_label, y_label, save_file_name):

    # Create the box plot
    plt.figure(figsize=(8, 6))  # Set the figure size
    sns.boxplot(x=x_label, y=y_label, data=df)

    # Add title and labels
    # plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.savefig(save_file_name)

if __name__ == "__main__":
    create_box_plot(df, title, x_label, y_label, save_file_name)