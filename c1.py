from scipy import signal
from curves import *
from TEST_ST import *



def C1(t,w,Fs):
    Maxc = maxc(t,w,Fs)

    locs_c1,pks_c1=signal.find_peaks(Maxc,height=[4.8,200]) 
    len_c1=len(locs_c1)

    return locs_c1,pks_c1,len_c1

def C2_3(t,w,Fs):

    Stdcl,Stdch =stdc(t,w,Fs)

    #obtener los valores de pico para STDC 

    locs_c2,pks_c2=signal.find_peaks(Stdcl,height=[0.2,100])
    len_c2=len(locs_c2)

    #obtener los valores pico para STDC de alta frecuencia

    locs_c3,pks_c3=signal.find_peaks(Stdch,height=[3.6,100]) 
    len_c3=len(locs_c3)

    locs = [locs_c2,locs_c3]
    len2_3 = [len_c2,len_c3]
    return locs,pks_c2,pks_c3,len2_3

def C4(t,w,Fs,f):
    C5=1
    Func = func(t,w,Fs,f)

    c4_i= np.mean(Func)
    if np.ceil(c4_i)==170:
        c4_i=170
    elif np.floor(c4_i)==170:
        c4_i=170

    kmin=np.argmin(Func)
    kmax=np.argmax(Func)

    ## chequeo para que no hayan cosas raras.
    if c4_i < 110*np.sqrt(2):
        if kmin<32:
            kmin=32
        elif kmin>len(Func)-32:
            kmin=len(Func)-32

        for k in range(kmin-32,kmin+31):
            C5=C5+(w[k])**2
        print(np.sqrt(C5/64),'\n')
        C5=np.sqrt(C5/64)/(120)
    elif c4_i > 110*np.sqrt(2):
        if kmax<32:
            kmax=32
        elif kmax>len(Func)-32:
            kmax=len(Func)-32
        for k in range(kmax-32,kmax+31):
            C5=C5+(w[k])**2
        print(np.sqrt(C5/64),'\n')
        C5=np.sqrt(C5/64)/(120)
    return c4_i,C5



