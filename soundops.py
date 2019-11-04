from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt
def frequency_extraction(audio, samplingrate):
    #steps in fourier transform
    #1. calculate amplitude of frequencies
    #2. calculate frequencies
    #3. return frequencies and amplitudes
    amplitudes = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(amplitudes))
    freqs=freqs*samplingrate
    return (freqs, amplitudes)
def gen_specgram(audiodata, windowlength, samplingrate):
    fig,ax=plt.subplots(1)
    pxx, freqs, bins,im=plt.specgram(audiodata,NFFT=windowlength,Fs=samplingrate)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.axis('off')
    plt.savefig("image.png", frameon='false')
#def trim_frequencies(frequencies, amplitudes, num_frequencies):
#    ##returns num_frequencies amount of frequencies w/ corresponding amplitudes
#    # find the lowest high frequency cap
#    largestfreq
#    for i in range(num_frequencies):
#        largest_idx=np.argmax(amplitudes)
#        largestfreqs.append(frequencies[largest_idx])
#        
def data_to_chunks(audiodata, size_of_chunk):
    audiodata=audiodata[:-(len(audiodata)%size_of_chunk)]
    newarray=np.split(audiodata, len(audiodata)/size_of_chunk) ##Timesteps of size size_of_chunk
    return newarray
def process_all(filename):
    samplingrate, audiodata = read(filename)
    chunkarray=data_to_chunks(audiodata, samplingrate)
    finalarray=[]
    for i in chunkarray:
        finalarray.append(frequency_extraction(i, samplingrate))
    return finalarray
def create_noise(audiodata):
    noise=np.random.normal(0,1, audiodata.shape)
    return audiodata+noise
def export_to_wav(audiodata,filename, samplingrate):
    write(filename, samplingrate,audiodata)

