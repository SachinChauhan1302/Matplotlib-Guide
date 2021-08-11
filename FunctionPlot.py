import matplotlib.pyplot as plt 
import numpy as np
#draw sine and cosine functions in the same plot.

X = np.linspace(-np.pi, np.pi,256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.xlim(X.min()*1.1,X.max()*1.1)
plt.ylim(-1,1)
plt.plot(X,C,color="red",linewidth=2.0,linestyle=":",label="cosine")
plt.plot(X,S,label="sine")

#adding legend to the chart
plt.legend(loc="upper left")


#adding annotation in chart
t = 2*np.pi/3
plt.annotate("example",xy=(1,0),xytext=(1, 0),arrowprops=dict(facecolor='black', shrink=0.05),)

#A comment added to test git

plt.show()


