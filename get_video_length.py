import ffmpeg
import os
import datetime
import math

VIDEO_DIR = "Jenkins_Course"
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


def format_duration(x):
    if x == 0:
        return "0:0:0"
    else:
        return str(datetime.datetime.strptime(str(datetime.timedelta(seconds=x)), "%H:%M:%S.%f").strftime("%H:%M:%S"))


num_files = get_num_files(VIDEO_DIR)
print("num_files:", num_files)
for duration in get_durations_lazy(VIDEO_DIR):
    print("\rDuration:", format_duration(length), perc(current_file, num_files), end="")
    length += duration
    current_file += 1


    #
    # metadata = ffmpeg.probe(filename)["streams"]
    #         duration = metadata[0]["duration"]
    #         length += float(duration)
    #         current_file += 1
    #         print("\r", format(length), perc(current_file, num_files), end="")
