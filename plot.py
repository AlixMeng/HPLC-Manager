import numpy as np
import matplotlib.pyplot as plt

Time = [0, 12, 24, 36, 48, 60, 72, 84, 96]
OD600 = [0.1, 3, 5, 10, 12, 15, 18, 20, 25]
Xylose = [40, 36, 25, 15, 5, 2, 1, 0, 0]
Ethanol = [0, 2, 5, 9, 10, 11, 12, 12, 12]
Xylitol = [0, 1, 1.5, 1.8, 2.0, 2.1, 2.2, 2.3, 10]
Acetate = [0, 0.5, 1.0, 1.2, 1.5, 1.8, 1.9, 2.0, 2.1]

fig, ax1 = plt.subplots(figsize=(7, 6))

ax1.plot(Time, Xylose, 'bv', markersize=10, label='Xylose')  # blue and symbol o
ax1.plot(Time, Xylose, '-', linewidth=3.0,
         color='b')  # '-' means solid line. Linewidth is 2.0. Color of the line is blue.
ax1.plot(Time, Ethanol, 'r^', markersize=10, label='Ethanol')  # red and symble triangle up
ax1.plot(Time, Ethanol, '-', linewidth=3.0, color='r')
ax1.plot(Time, OD600, 'ko', markersize=10, label='OD600')  # red and symble triangle up
ax1.plot(Time, OD600, '-', linewidth=3.0, color='k')
ax1.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.5, fontsize=15)

ax1.set_xlabel('Time(h)', fontsize=15)
ax1.set_ylabel('OD600, Xylose and Ethanol (g/L)', fontsize=15)
ax1.tick_params(direction="in", labelsize=14, size=5)

ax2 = ax1.twinx()
ax2.plot(Time, Xylitol, 'cp', markersize=10, label='Xylitol')
ax2.plot(Time, Xylitol, '-', linewidth=3.0, color='c')
ax2.plot(Time, Acetate, 'g*', markersize=10, label='Acetate')
ax2.plot(Time, Acetate, '-', linewidth=3.0, color='g')
ax2.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.5, fontsize=15)

ax2.set_ylabel('Xylitol and Acetate (g/L)', fontsize=15)
ax2.tick_params(direction="in", labelsize=15, size=5)

fig.tight_layout()
plt.savefig('plot1.png')
plt.show()