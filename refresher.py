#Jakub Kolasinski
#FE595 Python Refresher

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.title('Plot of one period of sine and cosine')
plt.xlabel('0 to 2π')
plt.legend(['sin(x)', 'cos(x)'])    
plt.show()

