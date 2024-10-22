import matplotlib.pyplot as plt
import squarify
import seaborn as sns

# Example word frequencies (percentages don't need to sum to 100)
labels = ['anxiety (4.0%)', 'back pain (3.7%)', 'care plan', 'Word D', 'Word E']
frequencies = [20, 30, 15, 25, 10]
save_file_name = 'chart_styles/tree_map/tree_map.png'
title = "Word Treemap"


def create_tree_map(labels, frequencies, title, save_file_name):

  # Set Seaborn style
  sns.set(style="whitegrid")

  # Create the treemap
  plt.figure(figsize=(11, 6))
  squarify.plot(sizes=frequencies, label=labels, alpha=0.8, color=sns.color_palette('Set2'), 
              text_kwargs={'fontsize': 14}) 

  # Formatting
  plt.axis('off')  # No axes
  plt.title(title)
  plt.savefig(save_file_name)


if __name__ == "__main__":
    create_tree_map(labels, frequencies, title, save_file_name)