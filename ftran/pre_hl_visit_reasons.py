from chart_styles.tree_map.tree_map import create_tree_map
import pandas as pd


df = pd.read_excel('data/pre_visit_reasons.xlsx')

name_list = df['term'].to_list()
perc_list = df['perc']

combined = [f'{x}\n({round(y, 1)})%' for x, y in zip(name_list, perc_list)]



# save the file
labels = combined
frequencies = perc_list
save_file_name = 'outputs/tree_map.png'
create_tree_map(labels, frequencies, "Visit Reason Treemap", save_file_name)