from get_video_length import GetVideoLength


def test_get_video_length():
    get_video_length = GetVideoLength("video_test")
    assert get_video_length.num_files() > 0
    expected = [
        "num_files: 2\n",
        "\rDuration: 0:00:09 50%",
        "\rDuration: 0:00:30 100%"
    ]
    seconds = 30.447533
    rows = list(get_video_length.sum_durations())
    assert rows == expected
    assert get_video_length.get_sum_durations_in_seconds() == seconds
