import unittest

from cs6515_raquels_blocks import RaquelsBlocks


class TestRaquelsBlocks(unittest.TestCase):
    def test_base_case_1(self):
        median = RaquelsBlocks([1, 2], [5, 4, 3])

        self.assertEqual(median, 3)

    def test_base_case_2(self):
        median = RaquelsBlocks([1, 2, 3], [5, 4])

        self.assertEqual(median, 3)


if __name__ == "__main__":
    unittest.main()
