from Video import Video

video = Video(".")
for data in video.get_data():
    print("\rFull Duration:", data["formatted_full_length"], data["ratio_index"], data["perc_index"], end="")
