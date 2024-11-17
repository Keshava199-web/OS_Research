import numpy as np
import matplotlib.pyplot as plt

# Data for travel and waiting times before and after AI implementation
before_implementation = [60, 30]  # [Travel Time (min), Waiting Time (min)]
after_implementation = [45, 25]   # [Travel Time (min), Waiting Time (min)]

# Labels and data
labels = ['Travel Time (min)', 'Waiting Time (min)']
x = np.arange(len(labels))

# Plotting the bar chart
fig, ax = plt.subplots()
bar_width = 0.35
ax.bar(x - bar_width/2, before_implementation, bar_width, label='Before Implementation')
ax.bar(x + bar_width/2, after_implementation, bar_width, label='After Implementation')

# Adding labels
ax.set_xlabel('Metrics')
ax.set_ylabel('Time (in minutes)')
ax.set_title('Traffic Flow Before and After AI Implementation')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
