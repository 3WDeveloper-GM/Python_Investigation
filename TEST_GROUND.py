from random import random 
from FUNCTION_PERTURBATIONS import *
from curves import *
from c1 import *
from Stockwellnice import *

import csv 

w=np.loadtxt('/home/glopez/Documentos/UNAH/1P2022/PROCESAMIENTO DIGITAL DE LA SEÑAL/CODE_PROY/sample5')
w=(w-np.mean(w))*(5.0/1023.0)*110*np.sqrt(2)
t=np.linspace(0,len(w),len(w))*1/4500

ff=60
A=120*np.sqrt(2)
t1=0
t2=0+(5/60-0)*random()
t3=t2+2/60+(8/60-t2-2/60)*random()
t4=8/60
al=1*(0.1+(0.9-0.1)*random())
Fs = 4500
arm1=0*(1.7+(10.2-1.7)*random())
arm2=0*(1.7+(10.2-1.7)*random())
ftran=600+(1000-600)*random()
fmin=0
fmax=Fs/2
tau=8/1000+(40/1000-8/1000)*random()
theta=0+(3.1415-0)*random()

#t,w = osc_tran(ff,A,t1,t2,t3,t4,al,Fs,arm1,arm2,ftran,tau)
#t,w = mag_pert_dist(ff,A,t1,t2,t3,t4,al,Fs,arm1,arm2,theta)

CURVESD(t,w,Fs,ff,fmin,fmax)
#graph(t,w,Fs)
locsc1,pksc1,le1=C1(t,w,Fs)
print(locsc1, '\n' ,  pksc1['peak_heights'], '\n' , le1,'\n')

locsc2,pksc2,pksc3,le2=C2_3(t,w,Fs)
print(locsc2[0], '\n','\n',pksc2['peak_heights'],'\n','\n',locsc2[1],'\n', pksc3['peak_heights'], '\n','\n', le2)

c4,C5=C4(t,w,Fs,ff)
print(c4,C5)