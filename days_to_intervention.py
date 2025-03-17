from chart_styles.box_plot.box_plot import create_box_plot
import pandas as pd
import os


data_dir = "/Users/z5116060/Desktop/GitProjects/hearing/data"

df = pd.read_excel(os.path.join(data_dir, 'intervention_day_count.xlsx'))

# save the file
save_file_name = 'outputs/box_plot.png'
create_box_plot(df, "Days from query to intervention", "GENDER_TEXT", "days_apart", save_file_name)