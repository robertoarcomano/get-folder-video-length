import pytest

from Video import Video


@pytest.fixture
def video():
    return Video("../")


def test_video(video):
    last_percent = ""
    for data in video.get_data():
        last_percent = data["perc_index"]
        print("Full Duration:", data["formatted_full_length"], data["ratio_index"], data["perc_index"])
    assert last_percent == "100%"

