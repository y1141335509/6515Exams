import unittest

from cs6515_tim_coffee import TimCoffee

from graph.digraph import DiGraph


class TestTimCoffee(unittest.TestCase):
    def test_base_case_1(self):
        graph = DiGraph([("a", "b"), ("b", "c"), ("c", "d")])
        lengths = {("a", "b"): 1, ("b", "c"): 1, ("c", "d"): 1}

        coffee_shops = {"b": 5, "c": 1}
        best, path = TimCoffee(
            graph, s="a", t="d", lengths=lengths, coffee_shops=coffee_shops
        )

        self.assertEqual(best, "b")
        self.assertEqual(path, ["a", "b", "c", "d"])

    def test_base_case_2(self):
        graph = DiGraph([("a", "b"), ("b", "c"), ("c", "d")])
        lengths = {("a", "b"): 1, ("b", "c"): 1, ("c", "d"): 1}

        coffee_shops = {"b": 1, "c": 5}
        best, path = TimCoffee(
            graph, s="a", t="d", lengths=lengths, coffee_shops=coffee_shops
        )

        self.assertEqual(best, "c")
        self.assertEqual(path, ["a", "b", "c", "d"])


if __name__ == "__main__":
    unittest.main()
