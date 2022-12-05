import ffmpeg
import os
import datetime
import math
import sys


def get_video_files(directory):
    video_files = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            filename = os.path.join(root, name)
            if ".mp4" in filename:
                video_files.append(filename)
    return video_files


def calc_duration(filename):
    return float(ffmpeg.probe(filename)["streams"][0]["duration"])


def perc(curr, num):
    return str(math.ceil(curr * 100 / num)) + "%"


def format_duration(x):
    return str(
        datetime.datetime.strptime(
            str(
                datetime.timedelta(seconds=math.floor(x))
            )
            , "%H:%M:%S"
        )
        .strftime("%H:%M:%S")
    )


if __name__ == "__main__":
    length = 0
    current_file = 0
    VIDEO_DIR = ""
    try:
        VIDEO_DIR = sys.argv[1]
    except IndexError:
        print("Syntax: ", sys.argv[0], "<Video Directory>")
        exit(-1)
    videos = get_video_files(VIDEO_DIR)
    num_videos = len(videos)
    print("Video Files:", num_videos)
    for duration in map(calc_duration, videos):
        length += duration
        current_file += 1
        print("\rDuration:", format_duration(length), perc(current_file, num_videos), end="")
    print()


