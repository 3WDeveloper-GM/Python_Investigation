import numpy as np
import matplotlib.pyplot as plt
from curves import*
from matplotlib.gridspec import GridSpec
import os
def CURVESD(t,w,Fs,ff,fmin,fmax):
    STA=sta(t,w,Fs)
    MAXC=maxc(t,w,Fs)
    STDLC, STDHC = stdc(t,w,Fs)
    FUNC = func(t,w,Fs,ff)



    ay = len(STDLC)
    extent = (t[0], t[-1], fmin, fmax)
    f=np.linspace(0,Fs/2,ay)



    fig =plt.figure()
    gs=GridSpec(nrows=3,ncols=2)
    ax1 = fig.add_subplot(gs[0,0])
    ax1.plot(t,w)
    ax1.grid(True)
    ax1.set_yticks(np.linspace(np.ceil(np.min(w)),np.ceil(np.max(w)),5))
    plt.setp(ax1.get_xticklabels(), visible=False)
    ax1.set(ylabel='Amplitud (V)')
    ax1.axis('tight')
    ax1.set_xlim(t[0],t[-1])

    extent=(t[0],t[-1],0,Fs/2)

    ax2 = fig.add_subplot(gs[1:,0],sharex=ax1)
    ax2.imshow(STA,origin='lower',aspect='auto',extent=extent)
    ax2.set(xlabel='Tiempo (s)',ylabel='Frecuencia (Hz)')

    ax3 = fig.add_subplot(gs[0,1])
    ax3.plot(f,MAXC)
    ax3.set(ylabel='Amplitud (V)')
    ax3.grid(True)
    ax3.set_yticks(np.linspace(0,np.ceil(np.max(MAXC)),5))
    ax3.set_xlim(f[0],f[-1])
    plt.setp(ax3.get_xticklabels(), visible=False)


    ax4 = fig.add_subplot(gs[1,1],sharex=ax3)
    ax4.plot(f,STDHC,f,STDLC)
    ax4.set(xlabel='Frecuencia (Hz)',ylabel='Amplitud (V)')
    ax4.grid(True)


    ax5 = fig.add_subplot(gs[2,1])
    ax5.plot(t,FUNC)
    ax5.set_ylim(min(FUNC)-0.08*min(FUNC),max(FUNC)+0.08*max(FUNC))
    ax5.set_xlim(t[0],t[-1])
    ax5.set_yticks(np.linspace(np.ceil(np.min(FUNC))-15,np.ceil(np.max(FUNC))+15,5))
    ax5.set(xlabel='Tiempo (s)', ylabel='Amplitud (V)')
    ax5.grid(True)

    plt.tight_layout()
    plt.savefig('./graph.png',dpi=150)