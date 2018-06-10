import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000) #return numbers over evenly spaced intervel
plt.plot(x, x, label="linear")#plots data x by x
plt.legend()#adds legend
plt.show()#displaygraph
