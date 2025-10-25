import unittest

from cs6515_business_division import BusinessDivision


class TestBusinessDivision(unittest.TestCase):
    def test_base_case_1(self):
        possible, _, _ = BusinessDivision((1, 2))

        self.assertFalse(possible)

    def test_base_case_2(self):
        input = (1, 1)

        possible, child1, child2 = BusinessDivision(input)

        self.assertTrue(possible)

        sum1 = sum([input[i] for i in child1])
        sum2 = sum([input[i] for i in child2])

        self.assertEqual(sum1, sum2)

    def test_base_case_3(self):
        input = (3, 1, 1, 2, 2, 1)

        possible, child1, child2 = BusinessDivision(input)

        self.assertTrue(possible)

        sum1 = sum([input[i] for i in child1])
        sum2 = sum([input[i] for i in child2])

        self.assertEqual(sum1, sum2)

    def test_base_case_4(self):
        input = (2, 3, 6)

        possible, child1, child2 = BusinessDivision(input)

        self.assertFalse(possible)

        sum1 = sum([input[i] for i in child1])
        sum2 = sum([input[i] for i in child2])

        self.assertEqual(sum1, sum2)

if __name__ == "__main__":
    unittest.main()
