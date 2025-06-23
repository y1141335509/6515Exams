def max_likeness(Vol, W, L, V, K):
    n = len(Vol)
    T = [[[0 for _ in range(K+1)] for _ in range(V+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for v in range(V+1):
            for k in range(K+1):
                if Vol[i-1] > v or W[i-1] > k:
                    T[i][v][k] = T[i-1][v][k]
                else:
                    T[i][v][k] = max(
                        T[i-1][v][k],
                        T[i-1][v - Vol[i-1]][k - W[i-1]] + L[i-1]
                    )
    return T[n][V][K]


print(max_likeness(Vol=[20,10,40,50], W=[2,3,5,6], L=[3,2,3,2], V=60, K=6))