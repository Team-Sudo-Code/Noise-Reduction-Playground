from pydub import AudioSegment
import glob
files = glob.glob('')
for file in files:
    newAudio = AudioSegment.from_wav(file)[0:10000] # milliseconds
    newAudio.export('./new/'+file.getName(), format="wav") # Exports to a wav file to a different path