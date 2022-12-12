import ffmpeg
import os
import datetime
import math
import sys


class Video:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files = ()
        self.get_files()

    def get_files(self):
        def walk_exception(x):
            raise x
        temporary_list = []
        for root, dirs, files in os.walk(self.dir_path, onerror=walk_exception):
            for name in files:
                filename = os.path.join(root, name)
                if ".mp4" in filename:
                    temporary_list.append(filename)
        self.files = tuple(temporary_list)

    def get_len(self):
        return len(self.files)

    def get_perc(self, index):
        return str(round(index * 100 / self.get_len())) + "%"

    @staticmethod
    def format_duration(x, print_format):
        return str(
            datetime.datetime.strptime(
                str(
                    datetime.timedelta(seconds=round(x))
                )
                , "%H:%M:%S"
            )
            .strftime(print_format)
        )

    def get_data(self, print_format="%H:%M:%S"):
        index = -1
        full_length = 0
        for file in self.files:
            index += 1
            length = float(ffmpeg.probe(file)["streams"][0]["duration"])
            full_length += length
            formatted_full_length = self.format_duration(full_length, print_format)
            perc_index = self.get_perc(index + 1)
            yield {
                "index": index,
                "length": length,
                "full_length": full_length,
                "formatted_full_length": formatted_full_length,
                "ratio_index": str(index + 1) + "/" + str(self.get_len()),
                "perc_index": perc_index
            }


if __name__ == "__main__":
    video = None
    try:
        video = Video(sys.argv[1])
    except IndexError:
        print("Syntax: ", sys.argv[0], "<Video Directory>")
        exit(-1)
    except Exception as ex:
        print(ex)
        exit(-2)
    for data in video.get_data():
        print("\rFull Duration:", data["formatted_full_length"], data["ratio_index"], data["perc_index"], end="")
    print()


