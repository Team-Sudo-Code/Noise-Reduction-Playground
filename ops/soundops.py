from scipy.io.wavfile import read
import numpy as np

def frequency_extraction(audio, samplingrate):
    #steps in fourier transform
    #1. calculate amplitude of frequencies
    #2. calculate frequencies
    #3. return frequencies and amplitudes
    amplitudes = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(amplitudes))
    freqs=freqs*samplingrate
    return (freqs, amplitudes)
def data_to_chunks(audiodata, samplingrate):
    newsamplerate=20*(samplingrate/1000) #20ms per sample
    newarray=np.split(audiodata, newsamplerate)
    return newarray
def process_all(audiodata, samplingrate):
    chunkarray=data_to_chunks(audiodata, samplingrate)
    finalarray=[]
    for i in chunkarray:
        finalarray.append(frequency_extraction(i, samplingrate))
    return finalarray

samplingrate, audiodata = read("basictone.wav")
freq=process_all(audiodata, samplingrate)
