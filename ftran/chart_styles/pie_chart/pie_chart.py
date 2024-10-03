# Branch push
import matplotlib.pyplot as plt

labels = 'Diagnosis', 'Visit Reason', 'Medicare Code', 'Other'
sizes = [45, 30, 15, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.savefig('pie_chart.png')