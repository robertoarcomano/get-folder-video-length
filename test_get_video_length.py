from get_video_length import GetVideoLength


def test_get_video_length():
    get_video_length = GetVideoLength("video_test")
    assert get_video_length.no_files() is False
    expected = [
        "num_files: 2\n",
        "\rDuration: 0:00:00 0%",
        "\rDuration: 0:00:09 50%"
    ]
    rows = list(get_video_length.sum_durations())
    assert rows == expected
