import pydub 
import numpy as np
from scipy.io.wavfile import read

def read(filepath):
    """Reads a .wav file to a numpy array"""
    data=read(filepath)
    return np.array(data[1], dtype=float)