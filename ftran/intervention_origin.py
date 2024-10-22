from chart_styles.pie_chart.pie_chart import create_pie_chart
import pandas as pd


df = pd.read_excel('data/intervention_origin.xlsx')


# save the file
save_file_name = 'outputs/intervention_origin_pie_chart.png'

perc_list = [100*num/(df['Total'].sum()) for num in df['Total'].tolist()]

combined = [f'{x}\n({round(y, 1)})%' for x, y in zip(df['Mapped'].to_list(), perc_list)]

create_pie_chart(combined, df['Total'], save_file_name)