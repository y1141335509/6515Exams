import unittest

from cs6515_friendly_competition import FriendlyCompetition


class TestFriendlyCompetition(unittest.TestCase):
    def test_base_case_1(self):
        result = FriendlyCompetition([3, 2, 1, 0])

        self.assertEqual(result, 0)

    def test_base_case_2(self):
        result = FriendlyCompetition([0, 1, 2, 3])

        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
