

def solution(P: list[int], f: float) -> int:
    if len(P) < 2:
        return 0
        
    n = len(P)
    T = [0] * n  # T[i] represents max profit up to day i
    
    for i in range(1, n):
        # Keep previous profit
        T[i] = T[i-1]
        
        # Try to sell on day i
        # Check all possible buying days before i
        for j in range(i):
            profit_from_trade = P[i] - P[j] - f  # Buy at j, sell at i
            total_profit = T[j] + profit_from_trade
            T[i] = max(T[i], total_profit)
    
    return T[n-1]



if __name__ == "__main__":
    # Example usage
    alist = [7, 1, 5, 3, 6, 4]
    result = solution(alist, .5)
    print(result)  # Expected output: (1, 5)

    alist = [9, 5, 8, 10, 11, 7, 3, 8, 9]
    print(solution(alist, .5))





