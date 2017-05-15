import wave
import matplotlib.pyplot as plt
import numpy as np
import os
def waveget(ks):
    f = wave.open(ks, "rb")

    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]

    str_data = f.readframes(nframes)
    f.close()

    wave_data = np.fromstring(str_data, dtype=np.short)
# print wave_data.shape
# print framerate
# print nframes
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    time = np.arange(0, nframes) * (1.0 / framerate)
    plt.subplot(211)
    plt.plot(time, wave_data[0])
    plt.subplot(212)
    plt.plot(time, wave_data[1])
    plt.xlabel("time zone")

    figname = ".".join(ks.split(".")[:-1]) + ".tiff"
    print figname
    plt.savefig(figname)

    
ks = "/Users/zhangjiawei/Documents/code/zjw/ximalaya"
wavs = os.listdir(ks)
for i in wavs:
    if i.endswith(".wav"):
        pks = ks + "/" + i
        waveget(pks)
