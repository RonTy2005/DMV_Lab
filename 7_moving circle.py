import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Create circle points
theta = np.linspace(0, 2*np.pi, 100)
radius = 1

# Initial circle position
x_center = -10
y_center = 0

x = x_center + radius * np.cos(theta)
y = y_center + radius * np.sin(theta)

# Plot the circle
circle, = ax.plot(x, y, 'b')

# Animation function
def animate(frame):
    x_center = -10 + 0.1 * frame  # move along x-axis
    x = x_center + radius * np.cos(theta)
    y = y_center + radius * np.sin(theta)
    circle.set_data(x, y)
    return circle,

# Create animation
ani = FuncAnimation(
    fig,
    animate,
    frames=400,
    interval=20,
    blit=True
)

plt.show()
