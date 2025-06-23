

def coin_change1(coins, value):
    dp = [0 for _ in range(value + 1)]
    dp[0] = 1

    for coin in coins:
        for v in range(1, value + 1):
            if coin <= v:
                dp[v] = dp[v] + dp[v - coin]

    return dp[-1]


def coin_change2(coins, value, k):
    dp = [[False] * (value + 1) for _ in range(k + 1)]
    dp[0][0] = True

    for i in range(k + 1):
        for j in range(value + 1):
            if dp[i][j]:
                for coin in coins:
                    if j + 1 <= k and i + coin <= value:
                        dp[i+1][j+coin] = True
    
    for i in range(k + 1):
        if dp[i][value]:
            return True
    return False


def optimal_bst(words, frequencies):
    n = len(frequencies)
    dp = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + frequencies[i]

    def get_sum(i, j):
        return prefix_sum[j + 1] - prefix_sum[i]
    
    for i in range(n):
        dp[i][i] = frequencies[i]
        root[i][i] = i
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                cost = left + right + get_sum(i, j)
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    root[i][j] = r
    
    def build_tree(i, j):
        if i > j: return None
        r = root[i][j] 
        return (words[r], build_tree(i, r-1), build_tree(r+1, j))
    
    return dp[0][n-1], build_tree(0, n-1)



if __name__ == '__main__':
    coins = [1,2,5]
    value = 5
    k = 5
    print(coin_change1(coins, value))

    coins = [5, 10, 15]
    value = 55
    k = 5
    print(coin_change2(coins, value, k))

    words = ["begin", "do", "else", "end", "if", "then", "while"]
    frequencies = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]
    cost, tree = optimal_bst(words, frequencies)
    print("Optimal BST cost:", cost)
    print("Optimal BST tree:", tree)












































