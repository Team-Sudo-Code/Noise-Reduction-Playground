from pydub import AudioSegment
from scipy.io.wavfile import read, write
import glob


def trim_files():
    files = glob.glob("./*.wav*")
    for file in files:
        newAudio = AudioSegment.from_wav(file)[0:10000]  # milliseconds
        # exports to a .wav file to a different path
        newAudio.export(file.rsplit('\\', 1)[0] + "/new/" + file.rsplit('\\', 1)[1], format="wav")