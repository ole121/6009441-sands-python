import numpy as np
import matplotlib.pyplot as plt

# Quick sine wave
t = np.linspace(0, 2, 1000)  # 2 seconds, 1000 points
sine = np.sin(2 * np.pi * t)  # 1 Hz sine wave

plt.plot(t, sine)
plt.title('Simple Sine Wave')
plt.show()