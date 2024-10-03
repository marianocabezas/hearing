import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

patron_hl_data = pd.read_csv('/Users/z5116060/Desktop/GitProjects/hearing/ftran/chart_styles/hist_plot/hist_time_sample.csv')

# plt.figure(figsize=(10, 5))
sns.histplot(data=patron_hl_data, x='Days', hue='Gender', kde=True, binwidth=2, stat='percent')
plt.title('Days from first hearing loss mention to GP Intervention')
patron_hl_data['Gender'] = patron_hl_data['Gender'].astype('category')
plt.savefig('hist_chart.png')