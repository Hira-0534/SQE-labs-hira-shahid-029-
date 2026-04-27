import matplotlib.pyplot as plt
import numpy as np

# Updated Data for Uber vs inDrive
labels = [
    'Functional Suitability', 'Performance Efficiency', 'Compatibility', 
    'Usability', 'Reliability', 'Security', 'Maintainability', 'Portability'
]

# Ratings based on your comparison table
uber_ratings = [3, 4, 5, 3, 2, 4, 4, 5]
indrive_ratings = [4, 5, 5, 4, 4, 4, 4, 5]

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop"
uber_ratings += uber_ratings[:1]
indrive_ratings += indrive_ratings[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], labels)

# Plot Uber data (Blue)
ax.plot(angles, uber_ratings, color='blue', linewidth=2, label='Uber')
ax.fill(angles, uber_ratings, color='blue', alpha=0.25)

# Plot inDrive data (Orange)
ax.plot(angles, indrive_ratings, color='orange', linewidth=2, label='inDrive')
ax.fill(angles, indrive_ratings, color='orange', alpha=0.25)

# Add Legend and Title
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.title('ISO 25010 Quality Comparison: Uber vs inDrive', pad=20)

# Save the chart
file_name = "quality_radar_Uber_inDrive.png"
plt.savefig(file_name)
print(f"Success! Chart saved as {file_name}")
plt.show()