import subprocess
import os
import sys
# Pre...
textfile_path = 'absolute/path/to/videos.txt'
# Read the text file
with open(textfile_path) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like

files_list = [x.strip() for x in content]
# Extract audio from video.
# It already save the video file using the named defined by output_name.
for file_num, file_path_input in enumerate(files_list, start=1):
    # Get the file name withoutextension
    file_name = os.path.basename(file_path_input)
    if 'mouthcropped' not in file_name:
        raw_file_name = os.path.basename(file_name).split('.')[0]
        file_dir = os.path.dirname(file_path_input)
        file_path_output = file_dir + '/' + raw_file_name + '.wav'
        print('processing file: %s' % file_path_input)
        subprocess.call(
            ['ffmpeg', '-i', file_path_input, '-codec:a', 'pcm_s16le', '-ac', '1', file_path_output])
        print('file %s saved' % file_path_output)