import matplotlib.pylab as plt


plt.plot(["a_dep", "b_dep", "c_dep", "d_dep"], [1, 2, 3, 4], label="carnation")
plt.plot(["a_dep", "b_dep", "c_dep", "d_dep"], [10, 20, 30, 40], label="childrensday")
plt.legend(loc='upper right')
plt.show()