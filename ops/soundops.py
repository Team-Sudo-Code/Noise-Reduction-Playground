import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np

def frequency_extraction(audio, samplingrate):
    transform = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(transform))
    idx = np.argmax(np.abs(transform))
    freq = freqs[idx]*samplingrate
    return freq
    
def show_specgram(audiodata, samplingrate):
    plt.specgram(audiodata, samplingrate)


samplingrate, audiodata = read("basictone.wav")
freq=frequency_extraction(audiodata, samplingrate)
