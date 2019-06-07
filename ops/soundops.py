import numpy as np
import subprocess as sp

def audio_to_np(filename)
    FFMPEG_BIN = "ffmpeg.exe"

    command = [FFMPEG_BIN,
               '-i', filename,
               '-f', 's16le',
               '-acodec', 'pcm_s16le',
               '-ar', '44100',  # ouput will have 44100 Hz
               '-ac', '2',  # stereo (set to '1' for mono)
               '-']
    pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)
    raw_audio = pipe.proc.stdout.read(88200 * 4)
    audio_array = np.fromstring(raw_audio, dtype="int16")
    audio_array = audio_array.reshape((len(audio_array) / 2, 2))
    return audio_array
