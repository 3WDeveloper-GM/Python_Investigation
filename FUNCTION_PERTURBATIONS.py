import numpy as np
def escalon(t1,t2,t0,Fs):
    t=np.linspace(t1,t2,round((t2-t1)*Fs)) #genero el vector de datos muestrales
    x=1*(t>t0) #genera un vector que es 1 cuando t>t0
    return t,x

def mag_pert(f,A,t1,t2,t3,t4,al,Fs):
    t=np.linspace(t1,t4,round((t4-t1)*Fs))
    x=A*np.sin(2*3.1415*f*t)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    return t,x


def mag_pert_dist(f,A,t1,t2,t3,t4,al,Fs,arm1,arm2,theta):
    t=np.linspace(t1,t4,round((t4-t1)*Fs))
    x=A*np.sin(2*3.1415*f*t+theta)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    x=x+arm1*np.sin(2*3*3.1415*f*t+theta)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    x=x+arm2*np.sin(2*5*3.1415*f*t+theta)*(1+al*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    return t,x


def osc_tran(f,A,t1,t2,t3,t4,al,Fs,arm1,arm2,Ftran,tau):
    t=np.linspace(t1,t4,round((t4-t1)*Fs))

    alf=np.exp(np.log(al)*(t-t2)/tau)

    x=np.sin(2*3.1415*f*t)*(1+alf*np.sin(2*3.1415*Ftran*t)*(escalon(t1,t4,t2,Fs)[1]-1*escalon(t1,t4,t3,Fs)[1]))
    x=x+arm1*np.sin(2*3*3.1415*f*t)
    x=x+arm2*np.sin(2*5*3.1415*f*t)
    x=A*x
    return t,x