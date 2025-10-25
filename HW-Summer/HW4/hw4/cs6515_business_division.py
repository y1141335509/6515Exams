def BusinessDivision(A: tuple[int]) -> tuple[bool, list[int], list[int]]:
    total = sum(A)
    if total % 2 != 0:
        return False, [], []
    
    target = total // 2
    n = len(A)

    T = [[False] * (target + 1) for _ in range(n + 1)]
    T[0][0] = True

    # print(f"Target sum: {target}")
    for i in range(1, n + 1):
        for j in range(target + 1):
            if j < A[i - 1]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]

    # print("DP Table (T[i][j]):")
    # print("    ", end="")
    # for j in range(target + 1):
    #     print(f"{j:>4}", end="")
    # print()

    # for i in range(n + 1):
    #     print(f"{i:>3}:", end=" ")
    #     for j in range(target + 1):
    #         print("   T" if T[i][j] else "   F", end="")
    #     print()

    if not T[n][target]:
        return False, [], []
    
    subset1 = []
    i, j = n, target
    while i > 0 and j >= 0:
        if T[i][j] and not T[i - 1][j]:
            subset1.append(i - 1)
            j -= A[i - 1]
        i -= 1
    
    subset1_set = set(subset1)
    subset2 = [i for i in range(n) if i not in subset1_set]

    subset1.reverse()
    subset2.reverse()
    return True, subset1, subset2