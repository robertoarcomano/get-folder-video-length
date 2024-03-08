import ffmpeg
import os
import datetime
import math
import sys


class GetVideoLength:
    file_formats = [".mp4"]

    def __init__(self, video_directory):
        self.video_directory, self.num_files = video_directory, self.get_num_files(video_directory)

    def get_num_files(self, directory):
        n = 0
        for root, dirs, files in os.walk(directory):
            for name in files:
                filename = os.path.join(root, name)
                for file_format in self.file_formats:
                    if file_format in filename:
                        n += 1
                        break
        return n

    def no_files(self):
        return self.num_files == 0

    def get_durations(self):
        for root, dirs, files in os.walk(self.video_directory):
            for name in files:
                filename = os.path.join(root, name)
                if ".mp4" in filename:
                    yield float(ffmpeg.probe(filename)["streams"][0]["duration"])

    @staticmethod
    def perc(curr, num):
        return str(math.ceil(curr * 100 / num)) + "%"

    def show_duration(self):
        length = 0
        current_file = 0
        for duration in self.get_durations():
            print("\rDuration:", str(datetime.timedelta(seconds=length)).split(".")[0], self.perc(current_file, self.num_files),
                  end="")
            length += duration
            current_file += 1


if len(sys.argv) < 2:
    print("Syntax:", sys.argv[0], "<Video Directory>")
    exit(-1)

get_video_length = GetVideoLength(sys.argv[1])
if get_video_length.no_files():
    print("No video files in", sys.argv[1])
    exit(-2)
print("num_files:", get_video_length.num_files)
get_video_length.show_duration()


