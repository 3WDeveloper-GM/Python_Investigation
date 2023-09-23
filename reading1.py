import matplotlib.pyplot as plt
import numpy as np
import csv 
arr = np.zeros(534,dtype=float)
t = np.zeros(534,dtype=float)
with open('/home/glopez/Documentos/UNAH/1P2022/PROCESAMIENTO DIGITAL DE LA SEÑAL/test20_data.csv','r') as file:
    reader = csv.reader(file)
    x = 0 
    for row in reader:
        arr[x] = row[1]
        t[x] = row[0]
        x = x + 1

media = np.mean(arr)
for i in range(0,len(arr)):
    arr[i]=arr[i]-media
    arr[i]=(5.0/1023.0)*arr[i]

ti=t[0]
for i in range(0,len(t)):
    t[i]=t[i]-ti
    print(t[i])

plt.plot(t,arr)
plt.show()