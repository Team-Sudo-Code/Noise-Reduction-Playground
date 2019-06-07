from pydub import AudioSegment
import glob
path = 'fill this in'
files = glob.glob(path)
for file in files:
    newAudio = AudioSegment.from_wav(file)
    newAudio = newAudio[0:10000] # milliseconds
    newAudio.export('./new/'+file.getName(), format="wav") # Exports to a wav file to a different path