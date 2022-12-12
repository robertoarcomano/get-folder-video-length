import unittest
from Video import Video


class TestVideo(unittest.TestCase):
    def setUp(self):
        self.video = Video("../")

    def test_video(self):
        last_percent = ""
        for data in self.video.get_data():
            last_percent = data["perc_index"]
            print("Full Duration:", data["formatted_full_length"], data["ratio_index"], data["perc_index"])
        self.assertEqual(last_percent, "100%")

    def tearDown(self):
        del self.video


if __name__ == '__main__':
    unittest.main()
