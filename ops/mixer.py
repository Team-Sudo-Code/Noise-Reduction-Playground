from pydub import AudioSegment
import random


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