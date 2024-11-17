import matplotlib.pyplot as plt
# plt.switch_backend('TkAgg')  # or 'Qt5Agg' if using PyQt
# Data for pollution reduction percentages
labels = ['CO2 Reduction', 'NOx Reduction', 'PM2.5 Reduction']
sizes = [15, 10, 20]  # % reduction in pollutants

# pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
ax.axis('equal')  # Equal ratio ensures the pie chart is a perfect circle.

# Title for  chart
plt.title('Pollution Reduction Breakdown (in %) After AI Optimization')

# For Display chart
plt.show()
