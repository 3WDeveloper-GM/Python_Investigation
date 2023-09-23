import numpy as np


'''
Esta funcion se encarga de generar un escalon unitario en cualquier tiempo x0,
el objetivo de esta función es generar saltos discontinuos que pueden presentarse
cuando el sistema de potencia entra en comportamientos inestables dinámicamente.
'''

def escalon(t1,t2,t0,Fs):
    t=np.linspace(t1,t2,round((t2-t1)*Fs)) #genero el vector de datos muestrales
    x=1*(t>t0) #genera un vector que es 1 cuando t>t0
    return t,x


'''
Esta función es una función que busca generar una perturbación en la magnitud de una
señal simulada, simplemente lo que sucede es que en un tiempo entre t2 y t3 aparece una
disminución o aumento de la amplitud de la señal
'''
def mag_pert(f,A,t1,t2,t3,t4,al,Fs):
    t=np.linspace(t1,t4,round((t4-t1)*Fs))
    x=A*np.sin(2*3.1415*f*t)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    return t,x


'''
Esta función hace dos cosas, modela cambios en amplitud y además de eso, genera dos
funciones armónicas extra, que corresponden al quinto y tercer armónico de la función
original, en este caso, si no se coloca nada en el parametro al (identicamente igual a 0)
la función simplemente modela una señal con contribuciones armónicas en la tercera y 
quinta componentes de la señal.
'''
def mag_pert_dist(f,A,t1,t2,t3,t4,al,Fs,arm1,arm2,theta):
    t=np.linspace(t1,t4,round((t4-t1)*Fs))
    x=A*np.sin(2*3.1415*f*t+theta)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    x=x+arm1*np.sin(2*3*3.1415*f*t+theta)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    x=x+arm2*np.sin(2*5*3.1415*f*t+theta)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    return t,x


'''
Esta función modela un transitorio que oscila a una frecuencia mucho mayor que la
frecuencia de la red eléctrica, esto suele aparecer mucho cerca de instalaciones de 
potencia que son controladas por un elemento semiconductor
'''
def osc_tran(f,A,t1,t2,t3,t4,al,Fs,arm1,arm2,Ftran,tau):
    t=np.linspace(t1,t4,round((t4-t1)*Fs))

    alf=np.exp(np.log(al)*(t-t2)/tau)

    x=np.sin(2*3.1415*f*t)*(1+alf*np.sin(2*3.1415*Ftran*t)*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    x=x+arm1*np.sin(2*3*3.1415*f*t)
    x=x+arm2*np.sin(2*5*3.1415*f*t)
    x=A*x
    return t,x