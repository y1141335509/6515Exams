# {"!a", "b", "c"} = (!a v b v c)
Clause = set[str]

# [{"!a", "b", "c"}, {"a", "!b", "c"}] = (!a v b v c) ^ (a v !b v c)
CNF = list[Clause]

# {"a", "!b", "c"} = a, !b, c set to true, !a, b, !c set to false
Assignment = set[str]
