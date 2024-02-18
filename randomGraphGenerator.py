import random as r
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# Generate random xy value pairs
x_values = []
y_values = []
z_values = []
w_values = []

r.seed(2)
for i in range(2000):
    x_values.append(r.randint(0,100))
    y_values.append(r.randint(0,100))
    z_values.append(r.randint(0,100))
    w_values.append(r.randint(0,1000))

# Plot x, y pairs in matplotlib
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=0.5, color="red")

# Plot x, z pairs in matplotlib
fig, ax = plt.subplots()
ax.scatter(x_values, z_values, s=0.5, color="red")

# Plot y, z pairs in matplotlib
fig, ax = plt.subplots()
ax.scatter(y_values, z_values, s=0.5, color="red")

# Plot x, y pairs in matplotlib with connections based on w
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=0.5, color="red")
for i in range(len(w_values)):
    for j in range(i + 1, len(w_values)):
        if w_values[i] == w_values[j]:
            ax.plot([x_values[i], x_values[j]], [y_values[i], y_values[j]], color='red', linewidth=0.2)

# Plot x, z pairs in matplotlib with connections based on w
fig, ax = plt.subplots()
ax.scatter(x_values, z_values, s=0.5, color="red")
for i in range(len(w_values)):
    for j in range(i + 1, len(w_values)):
        if w_values[i] == w_values[j]:
            ax.plot([x_values[i], x_values[j]], [z_values[i], z_values[j]], color='red', linewidth=0.2)

# Plot y, z pairs in matplotlib with connections based on w
fig, ax = plt.subplots()
ax.scatter(y_values, z_values, s=0.5, color="red")
for i in range(len(w_values)):
    for j in range(i + 1, len(w_values)):
        if w_values[i] == w_values[j]:
            ax.plot([y_values[i], y_values[j]], [z_values[i], z_values[j]], color='red', linewidth=0.2)


# Plot x, y, z pairs in matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
scatter = ax.scatter(x_values, y_values, z_values, s = 0.5, color = "black")

# Plot x, y, z pairs in matplotlib and colour by weight, w
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection = "3d")
scatter = ax2.scatter(x_values, y_values, z_values, c = w_values, cmap = "viridis", s = 2)
plt.colorbar(scatter)

# Add lines connecting points based on w
for i in range(len(w_values)):
    for j in range(i + 1, len(w_values)):
       if w_values[i] == w_values[j]:
           ax2.plot([x_values[i], x_values[j]], [y_values[i], y_values[j]], [z_values[i], z_values[j]], color='red', linewidth = 0.2)

# Plot the highest connected motif
highestOcc = max(set(w_values), key = w_values.count) # Find the highest occuring w value
mask = [w == highestOcc for w in w_values] # Create mask for points with highest occuring w value
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection = "3d")
ax3.scatter(np.array(x_values)[mask], np.array(y_values)[mask], np.array(z_values)[mask], s = 50, color = "black")
for i in range(len(w_values)):
    for j in range(i + 1, len(w_values)):
        if w_values[i] == w_values[j] == highestOcc:
            ax3.plot([x_values[i], x_values[j]], [y_values[i], y_values[j]], [z_values[i], z_values[j]], color = "red", linewidth = 0.5)
ax3.set_axis_off()


# Print the plots
plt.show()
