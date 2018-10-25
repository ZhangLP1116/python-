import matplotlib.pyplot as plt

from random_walk import Randomwalk

rw = Randomwalk()
rw.fill_walk()

plt.plot(rw.x_values,rw.y_values,linewidth=1)
plt.show()
