import matplotlib.pyplot as plt
import numpy as np
import textwrap

# Example data with long labels
categories = [
    'Category A: This is a very long label that might need wrapping', 
    'Category B: Another lengthy label for demonstration purposes', 
    'Category C: Yet another long category name to test wrapping', 
    'Category D: Short label'
]
values = np.array([30, 60, 90, 20])

# Wrap the labels to a desired width (in characters)
wrapped_categories = [ "\n".join(textwrap.wrap(label, width=25)) for label in categories ]

# Compute relative fractions
total = values.sum()
fractions = values / total

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(wrapped_categories, values, color='skyblue')

# Add annotations for the relative fraction
for bar, fraction in zip(bars, fractions):
    ax.text(bar.get_width() + total * 0.02,
            bar.get_y() + bar.get_height() / 2, 
            f"{fraction:.1%}", 
            va='center', ha='left', fontsize=12, color='black')

ax.set_xlabel('Values')
ax.set_title('Horizontal Bar Chart with Multiline Labels')
plt.tight_layout()
plt.show()


