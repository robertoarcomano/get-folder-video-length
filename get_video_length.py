import ffmpeg
import os
import datetime
import math

VIDEO_DIR = "Jenkins_Course"
length = 0
current_file = 0


def get_video_files(directory):
    video_files = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            filename = os.path.join(root, name)
            if ".mp4" in filename:
                video_files.append(filename)
    return video_files


def get_duration(filename):
    return float(ffmpeg.probe(filename)["streams"][0]["duration"])


def perc(curr, num):
    return str(math.ceil(curr * 100 / num)) + "%"


def format_duration(x):
    if x == 0:
        return "0:0:0"
    else:
        return str(datetime.datetime.strptime(str(datetime.timedelta(seconds=x)), "%H:%M:%S.%f").strftime("%H:%M:%S"))


files = get_video_files(VIDEO_DIR)
for file in files:
    print("\rDuration:", format_duration(length), perc(current_file, len(files)), end="")
    length += get_duration(file)
    current_file += 1












    #
    # metadata = ffmpeg.probe(filename)["streams"]
    #         duration = metadata[0]["duration"]
    #         length += float(duration)
    #         current_file += 1
    #         print("\r", format(length), perc(current_file, num_files), end="")
