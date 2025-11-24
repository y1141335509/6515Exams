import unittest
from typing import Callable

from cs6515_double_sat import (
    input_transformation,
    output_transformation,
    verify_solution,
)

from npc.types import CNF, Assignment


class TestDoubleSat(unittest.TestCase):
    def test_base_case_1(self):
        cnf = [{"a", "b"}]
        assignments = ({"a", "!b"}, {"!a", "b"})

        self.assertTrue(verify_solution(cnf, assignments))

    def test_base_case_2(self):
        cnf = [{"a", "b"}]
        assignments = ({"a", "b"}, {"!a", "!b"})

        self.assertFalse(verify_solution(cnf, assignments))

    def test_base_case_3(self):
        cnf = [{"a", "b"}, {"a", "!b"}]
        assignments = ({"a", "b"}, {"a", "!b"})

        self.assertTrue(verify_solution(cnf, assignments))

    def test_base_case_4(self):
        def really_bad_double_sat(cnf: CNF) -> tuple[Assignment, Assignment] | None:
            """
            Returns a really bad guess at a solution for Double SAT.
            """
            variables = set()

            for clause in cnf:
                variables.update({literal.replace("!", "") for literal in clause})

            return (variables, {f"!{v}" for v in variables})

        cnf = [{"a", "b", "c"}, {"!a", "b"}, {"!c", "d"}]
        assignment = sat(cnf, really_bad_double_sat)

        self.assertEqual(len(assignment), 4)


def sat(
    cnf: CNF, double_sat: Callable[[CNF], tuple[Assignment, Assignment]]
) -> Assignment | None:
    """
    SAT solver that uses double_sat as a black box. This function is passed in and hidden from you.
    """
    # This is how we will run your functions for testing.
    return output_transformation(double_sat(input_transformation(cnf)))


if __name__ == "__main__":
    unittest.main()
