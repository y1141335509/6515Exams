def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize T with (n+1) x (capacity+1) filled with 0
    T = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the table
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], T[i-1][j - weights[i-1]] + values[i-1])

    # Print the T table
    print("Knapsack DP Table (T[i][j]):")
    print("    ", end="")
    for j in range(capacity + 1):
        print(f"{j:>3}", end="")
    print()
    for i in range(n + 1):
        print(f"{i:>3}:", end=" ")
        for j in range(capacity + 1):
            print(f"{T[i][j]:>3}", end="")
        print()
    
    print('\n Value of T[3,7] is: ', T[3][7])
    return T[n][capacity]

# Inputs
weights = [3, 4, 4, 6]
values  = [2, 3, 4, 1]
capacity = 8

# Run and get result
max_profit = knapsack(weights, values, capacity)
print("\nMaximum profit:", max_profit)