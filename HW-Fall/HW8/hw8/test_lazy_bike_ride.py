import unittest

from cs6515_lazy_bike_ride import LazyBikeRide

from graph.graph import Graph


class TestLazyBikeRide(unittest.TestCase):
    def test_base_case_1(self):
        graph = Graph([("a", "b"), ("b", "c"), ("c", "d")])
        lengths = {("a", "b"): 1, ("b", "c"): 1, ("c", "d"): 1}

        E_b = [("a", "b"), ("b", "c"), ("c", "d")]
        E_x = []

        routes = LazyBikeRide(graph, E_b, E_x, lengths)

        self.assertEqual(routes, [("a", "b"), ("b", "c"), ("c", "d")])

    def test_base_case_2(self):
        graph = Graph([("a", "b"), ("b", "c"), ("c", "d"), ("a", "d")])
        lengths = {("a", "b"): 2, ("b", "c"): 2, ("c", "d"): 2, ("a", "d"): 1}

        E_b = [("a", "b"), ("b", "c"), ("c", "d")]
        E_x = [("a", "d")]

        routes = LazyBikeRide(graph, E_b, E_x, lengths)

        self.assertEqual(routes, [("a", "b"), ("b", "c"), ("c", "d")])


if __name__ == "__main__":
    unittest.main()
