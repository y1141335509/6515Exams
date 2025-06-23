def HW0(A: tuple[int]) -> tuple[int, list[int]]:
    if not A: return 0, []

    size = len(A)
    dp = [1] * size
    prev = [-1] * size

    for i in range(1, size):
        for j in range(i):
            if A[i] > A[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_length = max(dp)
    max_index = dp.index(max_length)

    lis = []
    while max_index != -1:
        lis.append(max_index)
        max_index = prev[max_index]

    lis.reverse()

    return max_length, lis
