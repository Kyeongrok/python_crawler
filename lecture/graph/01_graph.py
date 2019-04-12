import numpy as np
import matplotlib.pylab as plt

'''
x = y
1   1
2   2
0.5 0.5
'''
x = np.arange(-5, 5, 0.1)
y = lambda x: np.array(x > 2, dtype=int)

print(y(x))

plt.plot(x, y(x))
plt.grid()
plt.show()