# Branch push
import matplotlib.pyplot as plt

save_file_name = 'chart_styles/pie_chart/pie_chart.png'

labels = 'Diagnosis', 'Visit Reason', 'Medicare Code', 'Other'
sizes = [45, 30, 15, 10]


def create_pie_chart(labels, sizes, save_file_name):
  fig, ax = plt.subplots()
  ax.pie(sizes, labels=labels)

  plt.savefig(save_file_name)

if __name__ == "__main__":
  create_pie_chart(labels, sizes, save_file_name)