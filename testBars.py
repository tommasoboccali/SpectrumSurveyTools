import matplotlib.pyplot as plt
import numpy as np

# Example data
categories = ['A', 'B', 'C', 'D']
values = np.array([30, 60, 90, 20])

# Compute relative fractions
total = values.sum()
fractions = values / total

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(categories, values, color='skyblue')

# Add annotations
for bar, fraction in zip(bars, fractions):
    ax.text(bar.get_width() + total * 0.02,  # Position text slightly right of bar
            bar.get_y() + bar.get_height()/2, 
            f"{fraction:.1%}",  # Format as percentage
            va='center', ha='left', fontsize=12, color='black')

# Labels and title
ax.set_xlabel('Values')
ax.set_title('Horizontal Bar Chart with Fractions')

plt.show()

