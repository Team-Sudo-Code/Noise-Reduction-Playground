import numpy as np
import subprocess

FFMPEG_BIN = "ffmpeg.exe"

command = [FFMPEG_BIN,
           '-i', 'mySong.mp3',
           '-f', 's16le',
           '-acodec', 'pcm_s16le',
           '-ar', '44100',  # ouput will have 44100 Hz
           '-ac', '2',  # stereo (set to '1' for mono)
           '-']
output=subprocess.run(command, capture_output=True)

