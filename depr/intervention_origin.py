# moved
from chart_styles.pie_chart.pie_chart import create_pie_chart
import pandas as pd
import os


data_dir = "/Users/z5116060/Desktop/GitProjects/hearing/data"

df = pd.read_excel(os.path.join(data_dir, 'intervention_origin.xlsx'))


# save the file
save_file_name = 'outputs/intervention_origin_pie_chart.png'

perc_list = [100*num/(df['Total'].sum()) for num in df['Total'].tolist()]

combined = [f'{x}\n({round(y, 1)})%' for x, y in zip(df['Mapped'].to_list(), perc_list)]

create_pie_chart(combined, df['Total'], save_file_name)