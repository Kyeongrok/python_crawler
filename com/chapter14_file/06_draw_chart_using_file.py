import numpy as np
import matplotlib.pylab as plt

f1 = open("./save_line.txt", mode='r')
lines = f1.readlines()

datas = [line.replace("\n", "") for line in lines]

plt.plot(np.arange(1, len(datas)+1, 1), datas)
plt.show()