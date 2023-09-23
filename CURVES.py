import numpy as np
from stockwell import st
from scipy import signal
def curvas(x,y,Fs,f):

    ##Filtrar la funcion original en 2 dominios
    ##baja
    b,a =signal.butter(4,275/1600,btype='low')
    zi=signal.lfilter_zi(b,a)
    ly,_=signal.lfilter(b,a,y,zi=zi*y[0])

    ##alta
    b,a =signal.butter(3,275/1600,btype='high')
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

    ##Generar la MAXC
    MAXC=np.mean(STA,axis=1)

    ##Generar la STDC de baja frecuencia
    STDCL=np.std(STA,axis=1)

    ##Generar la STDC de alta frecuencia
    STDCH=np.std(STAH,axis=1)

    ##Generar la FUNC
    ind=round(f*len(x)/Fs)
    FUNC=STA[ind][:]

    

    return STA,MAXC,STDCL,STDCH,FUNC