import numpy as np
import matplotlib.pyplot as plt


Fs=10;

n=np.linspace(0,99,100)
t=np.linspace(0,99,100)*(1/Fs)
y=np.cos(3.14159265*n/8)

f=t=np.linspace(0,99,100)*(Fs)

Y=np.fft.fft(y)

plt.plot(f,np.abs(Y))
plt.xlim(f[0],500)
plt.grid(True)
plt.xticks(np.linspace(0,500,20))
plt.show()