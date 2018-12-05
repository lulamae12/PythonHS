import pyaudio, scipy.io
import numpy as np
import matplotlib.pyplot as plt
CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
#make numoy array of volume
while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**16)
    print("#","%s"%(bars))
    plt.figure(1)
    plt.title('Signal Wave...')
    plt.plot(bars, peak, linestyle='-', marker='o', color='g')
    plt.pause(0.05)
plt.show()
stream.stop_stream()
stream.close()
p.terminate()
