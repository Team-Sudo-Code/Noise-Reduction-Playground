import glob


def main():
    files = glob.glob("./*.mp4")
    print("Discovered {} files".format(len(files)))
    for f in files:
        if f.lower()[-3:] == "mp4":
            print("processing {}".format(f))
            process(f)


def process(f):
    fin = f
    fout = f[:-3] + "mp3"
    cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 320k -f wav {}".format(fin, fout)
    os.popen(cmd)


main()
