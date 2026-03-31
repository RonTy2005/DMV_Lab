import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Straight Line Moving Left to Right")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")


line, = ax.plot([], [], 'r-', linewidth=2)


def init():
    line.set_data([], [])
    return line,


def update(frame):
    x = [frame, frame]   
    y = [0, 10]          
    line.set_data(x, y)
    return line,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                    init_func=init, blit=True, interval=50)

plt.show()
