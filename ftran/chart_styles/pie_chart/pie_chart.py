# Branch push
import matplotlib.pyplot as plt

labels = 'Reason 1', 'Reason 2', 'Reason 3', 'Other'
sizes = [45, 30, 15, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.savefig('pie_chart.png')