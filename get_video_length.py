import ffmpeg
import os
import datetime
import math
import sys

length = 0
current_file = 0


def get_num_files(directory):
    n = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            filename = os.path.join(root, name)
            if ".mp4" in filename:
                n += 1
    return n


def get_durations_lazy(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            filename = os.path.join(root, name)
            if ".mp4" in filename:
                yield float(ffmpeg.probe(filename)["streams"][0]["duration"])


def perc(curr, num):
    return str(math.ceil(curr * 100 / num)) + "%"


if len(sys.argv) < 2:
    print("Syntax:", sys.argv[0], "<Video Directory>")
    exit(-1)

VIDEO_DIR = sys.argv[1]
num_files = get_num_files(VIDEO_DIR)
if num_files == 0:
    print("No video files in", VIDEO_DIR)
    exit(-2)
print("num_files:", num_files)
for duration in get_durations_lazy(VIDEO_DIR):
    print("\rDuration:", str(datetime.timedelta(seconds=length)).split(".")[0], perc(current_file, num_files), end="")
    length += duration
    current_file += 1

