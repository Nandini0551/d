#DTFT Implementation
import numpy as np
from matplotlib import pyplot as plt
y=[]
x=[1,2,3,4]
w=np.arange(-np.pi,np.pi,0.01*np.pi)
for i in range(0,len(w)):
        s=0
        for n in range(0,len(x)):
                s=s+x[n]*np.exp(-1*1j*w[i]*n)
        y.append(s)
print(x)
plt.subplot(211)
plt.stem(w,np.abs(y))
plt.subplot(212)        
plt.stem(w,np.angle(y))          
plt.show()
