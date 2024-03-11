import ffmpeg
import os
import datetime
import math
import sys


class GetVideoLength:
    file_formats = [".mp4", ".avi"]
    filenames = []

    def __init__(self, video_directory):
        self.video_directory = video_directory
        self.get_filenames()

    def get_filenames(self):
        for root, dirs, files in os.walk(self.video_directory):
            for name in files:
                if any(file_format in name for file_format in self.file_formats):
                    self.filenames.append(os.path.join(root, name))

    def num_files(self):
        return len(self.filenames)

    def get_durations(self):
        for filename in self.filenames:
            yield float(ffmpeg.probe(filename)["streams"][0]["duration"])

    @staticmethod
    def perc(curr, num):
        return str(math.ceil(curr * 100 / num)) + "%"

    def sum_durations(self):
        length = 0
        current_file = 0
        yield "num_files: " + str(self.num_files()) + "\n"
        for duration in self.get_durations():
            length += duration
            current_file += 1
            yield "\rDuration: " + str(datetime.timedelta(seconds=length)).split(".")[0] + " " + \
                self.perc(current_file, self.num_files())

    def get_sum_durations_in_seconds(self):
        length = 0
        for duration in self.get_durations():
            length += duration
        return length


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Syntax:", sys.argv[0], "<Video Directory>")
        exit(-1)
    get_video_length = GetVideoLength(sys.argv[1])
    if not get_video_length.num_files():
        print("No video files in", sys.argv[1])
        exit(-2)
    for row in get_video_length.sum_durations():
        print(row, end="")
    print()
    print("Seconds:", get_video_length.get_sum_durations_in_seconds())
