from npc.types import CNF, Assignment, Clause


def verify_solution(cnf: CNF, assignments: tuple[Assignment, Assignment]) -> bool:
    """
    Verify that assignments is a valid Double SAT solution to the cnf.
    """
    # Write your verification here.
    a1, a2 = assignments

    if a1 == a2:
        return False
    
    def is_cnf_satisfies(assignment: Assignment, cnf: CNF) -> bool:
        for clause in cnf:
            satisfied = False
            for literal in clause:
                if literal in assignment:
                    satisfied = True
                    break
            if not satisfied:
                return False
        return True
    
    return is_cnf_satisfies(a1, cnf) and is_cnf_satisfies(a2, cnf)


def input_transformation(cnf: CNF) -> CNF:
    """
    Transform from a SAT input to a Double SAT input
    """
    # Write your transformation here.
    return cnf


def output_transformation(
    assignments: tuple[Assignment, Assignment] | None,
) -> Assignment | None:
    """
    Transform from a Double SAT output to a SAT output
    """
    # Write your transformation here.
    if not assignments:
        return None
    a1, a2 = assignments

    result = set()
    for literal in a1:
        var = literal.replace("!", "")
        if var and var[0].islower():
            result.add(literal)
    return result
