from chart_styles.bar_chart.bar_chart import create_bar_chart
import pandas as pd
import os

data_dir = "/Users/z5116060/Desktop/GitProjects/hearing/data"

df = pd.read_excel(os.path.join(data_dir, 'first_intervention_type.xlsx'))


# save the file
save_file_name = 'outputs/intervention_type_bar_chart.png'

perc_list = [100*num/(df['Total'].sum()) for num in df['Total'].tolist()]


new_df = pd.DataFrame({
  'Intervention Type': df['Intervention Type'],
  'Percentage (%)': perc_list
})

create_bar_chart(new_df, 'Intervention Type', 'Percentage (%)', save_file_name)