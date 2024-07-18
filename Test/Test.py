import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20, 0.1)
x = np.expand_dims(x, 1)
noise = np.random.randn(*x.shape)

y = 5 * x + 12 + noise

point = np.concatenate((x, y), axis=1)

plt.plot(x, y, 'bo')

plt.show()