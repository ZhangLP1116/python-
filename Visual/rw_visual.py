import matplotlib.pyplot as plt

from random_walk import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()
    
    plt.figure(figsize=(10,6))
    
    num_points = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,s=1,c=num_points,cmap=plt.cm.Blues)
    plt.scatter(0,0,c='red',s=40)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='yellow',s=40)
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    
    plt.show()
    
    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break

