from chart_styles.box_plot.box_plot import create_box_plot
import pandas as pd


df = pd.read_excel('data/intervention_day_count.xlsx')


# save the file
save_file_name = 'outputs/box_plot.png'
create_box_plot(df, "Days from query to intervention", "GENDER_TEXT", "days_apart", save_file_name)