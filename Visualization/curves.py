import numpy as np
from stockwell import st
from scipy import signal
def sta(x,y,Fs):
    ##Generar la Transformada de Stockwell primero
    fmin = 0  # Hz
    fmax = Fs/2  # Hz
    df = 1./(x[-1]-x[0])  # sampling step in frequency domain (Hz)
    fmin_samples = int(fmin/df)
    fmax_samples = int(fmax/df)

    ##Stockwell
    stock = st.st(y, fmin_samples, fmax_samples)

    ##Generar la STA 
    STA=np.abs(stock)
    return STA

def maxc(x,y,Fs):

    ##Generar la Transformada de Stockwell primero
    b=np.blackman(len(y))
    Aw=len(b)/np.sum(b)
    y=Aw*y*b
    fmin = 0  # Hz
    fmax = Fs/2  # Hz
    df = 1./(x[-1]-x[0])  # sampling step in frequency domain (Hz)
    fmin_samples = int(fmin/df)
    fmax_samples = int(fmax/df)

    ##Stockwell
    stock = st.st(y, fmin_samples, fmax_samples)

    ##Generar la STA 
    STA=np.abs(stock)

    ##Generar la MAXC de baja frecuencia
    MAXC=np.mean(STA,axis=1)

    return MAXC

def stdc(x,y,Fs):

    ##Filtrar la funcion original en 2 dominios
    ## frecuencia fundamental
    N,wn = signal.cheb2ord([55/(Fs/2),65/2250],[20/(Fs/2),110/(Fs/2)],4,20)
    b,a =signal.cheby2(N,30,wn,btype='bandpass')
    # print('COEFICIENTES DEL FILTRO PASA BAJA CHEBYSHEV DE TIPO 2','\n')
    # print('El orden del filtro es : ' , N)
    # print('Los coeficientes del numerador son: ' ,'\n', b, '\n')
    # print('Los coeficientes del denominador son: ','\n',a, '\n')
    #-------------------------------------------------------------
    # COEFICIENTES


    # a1 = -5.95201754
    # a2 =  14.78177563
    # a3 =  -19.60625566  
    # a4 = 14.64843897
    # a5= -5.84512348
    # a6=   0.97318241
    # b0 = 0.00130345 
    # b1 = -0.00519429
    # b2 =  0.0064783   
    # b3 = 0.0
    # b4 = -0.0064783   
    # b5 = 0.00519429
    # b6 =-0.00130345
    #ly=np.zeros(len(y),dtype=float)
    # for i in range(len(y)):
    #     if i<6:
    #         ly[i]=y[i]
    #     else:
    #         ly[i]=b0*y[i]+b1*y[i-1]+b2*y[i-2]+b3*y[i-3]+b4*y[i-4]+b5*y[i-5]+b6*y[i-6]-a1*ly[i-1]-a2*ly[i-2]-a3*ly[i-3]-a4*ly[i-4]-a5*ly[i-5]-a6*ly[i-6]
    # ly=ly/np.sqrt(len(ly))

    zi=signal.lfilter_zi(b,a)
    ly,_=signal.lfilter(b,a,y,zi=zi*y[0])

    ##alta
    b,a =signal.cheby2(3,30,325/1600,btype='high')
    # print('COEFICIENTES DEL FILTRO PASA ALTA CHEBYSHEV DE TIPO 2','\n')
    # print('Los coeficientes del numerador son: ' ,'\n', b, '\n')
    # print('Los coeficientes del denominador son: ','\n',a, '\n')
    zi=signal.lfilter_zi(b,a)
    hy,_=signal.lfilter(b,a,y,zi=zi*y[0])

    ##Generar la Transformada de Stockwell primero

    fmin = 0  # Hz
    fmax = Fs/2  # Hz
    df = 1./(x[-1]-x[0])  # sampling step in frequency domain (Hz)
    fmin_samples = int(fmin/df)
    fmax_samples = int(fmax/df)

    ##Stockwell de baja
    stock = st.st(ly, fmin_samples, fmax_samples)

    ##Stockwell de alta
    stockh = st.st(hy, fmin_samples, fmax_samples)

    ##Generar la STA de baja frecuencia
    STA=np.abs(stock)

    ##Generar la STA de alta frecuencia
    STAH=np.abs(stockh)

    ##Generar la STDC de baja frecuencia
    STDCL=np.std(STA,axis=1)

    ##Generar la STDC de alta frecuencia
    STDCH=np.std(STAH,axis=1)

    return STDCL, STDCH

def func(x,y,Fs,f):
    
    ##Generar la Transformada de Stockwell primero

    fmin = 0  # Hz
    fmax = Fs/2  # Hz
    df = 1./(x[-1]-x[0])  # sampling step in frequency domain (Hz)
    fmin_samples = int(fmin/df)
    fmax_samples = int(fmax/df)

    ##Stockwell
    stock = st.st(y, fmin_samples, fmax_samples)

    ##Generar la STA 
    STA=np.abs(stock)

    ##Generar la FUNC
    ind=round(f*len(x)/Fs)
    FUNC=STA[ind][:]

    return FUNC
