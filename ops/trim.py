from pydub import AudioSegment
import glob
files = glob.glob("/Users/alexa/OneDrive/Documents/GitHub/Audio-Segmentation/ops/*.wav*")
for file in files:
    newAudio = AudioSegment.from_wav(file)[0:10000]  # milliseconds
    # exports to a .wav file to a different path
    newAudio.export(file.rsplit('\\', 1)[0]+"/new/"+file.rsplit('\\', 1)[1], format="wav")


