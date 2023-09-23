from stockwell import st
import numpy as np
import matplotlib.pyplot as plt

def graph(t,w,Fs):
    ##Generar la Transformada de Stockwell primero

    fmin = 0  # Hz
    fmax = Fs/2  # Hz
    df = 1./(t[-1]-t[0])  # sampling step in frequency domain (Hz)
    fmin_samples = int(fmin/df)
    fmax_samples = int(fmax/df)

    ##Stockwell
    stock = st.st(w, fmin_samples, fmax_samples)

    ##Generar la STA 
    STA=np.abs(stock)

    extent=(t[0],t[-1],0,Fs/2)

    plt.imshow(STA,origin='lower',aspect='auto',extent=extent)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    cbar = plt.colorbar()
    cbar.ax.tick_params(labelsize=8)
    cbar.set_label('Amplitud (V)', rotation=270,fontsize=8)
    plt.tight_layout()
    plt.savefig('./stock.png',dpi=150)

