from pydub import AudioSegment
import random
import scipy
import numpy as np
from scipy.io.wavfile import read
import trim
import matplotlib.pyplot as plt


def audio_np_list(directory):
    nplist=[]
    pattern=directory+"/*.wav*"
    trim.trim_files(pattern)
    filenames=trim.find_matching(pattern)
    for i in filenames:
        nplist.append(read(filenames[i]))
    return nplist

def generate_rand_frequency():
    audio = AudioSegment.from_wav("basictone.wav")  # import in the file with a tone of 440 Hz
    octaves = random.randint(-30, 30) / 10 #generates a random number from -3 to 3
    new_sample_rate = int(audio.frame_rate * (2.0 ** octaves))
    changed_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
    changed_audio.export("test.wav", format="wav")

def combine_sounds(file1, file2, outputfile):
    #combines two tones
    sound1 = AudioSegment.from_file(file1)
    sound2 = AudioSegment.from_file(file2)
    combined = sound1.overlay(sound2)
    combined.export(outputfile, format='wav')
def fft_decompose(file, num_freqs):
    ##num freqs is number of frequencies to return
    final=[]
    frame_rate, audio_data = read(file)
    len_data = len(audio_data) #optimized code from stack overflow that performs fourier transform faster
    channel_1 = np.zeros(2 ** (int(np.ceil(np.log2(len_data)))))
    channel_1[0:len_data] = audio_data
    fft=np.fft.fft(channel_1)
    fftfreq=np.fft.fftfreq(len(fft))
    while num_freqs>=1:
        idx = np.argmax(np.abs(fft))
        freq = fftfreq[idx]
        final.append(abs(freq * frame_rate))
        fft[idx]=0
        num_freqs-=1
    return final
a=fft_decompose("combined.wav", 10)
