from chart_styles.tree_map.tree_map import create_tree_map
import pandas as pd
import os

data_dir = "/Users/z5116060/Desktop/GitProjects/hearing/data"

df = pd.read_excel(os.path.join(data_dir, 'pre_visit_reasons.xlsx'))

name_list = df['term'].to_list()
perc_list = df['perc']

combined = [f'{x}\n({round(y, 1)})%' for x, y in zip(name_list, perc_list)]



# save the file
labels = combined
frequencies = perc_list
save_file_name = 'outputs/tree_map_2.png'
create_tree_map(labels, frequencies, "Visit Reason Treemap", save_file_name)