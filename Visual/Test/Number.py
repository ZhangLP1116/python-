import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values=[x**3 for x in x_values]

plt.scatter(x_values,y_values,s=40,c=y_values,cmap=plt.cm.Reds)

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

plt.tick_params(axis='both',labelsize=14,which='major')
plt.axis([0,5001,0,125000000001])

plt.show()
