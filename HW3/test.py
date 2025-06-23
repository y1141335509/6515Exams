def find_missing_ap(S):
    n = len(S)
    d = (S[-1] - S[0]) // n  # n instead of (n-1) because one element is missing
    
    low, high = 0, n - 1
    
    while low < high:
        mid = (low + high) // 2
        expected = S[0] + mid * d
        if S[mid] == expected:
            low = mid + 1
        else:
            high = mid
    return S[0] + low * d

# Example tests
print(find_missing_ap([2, 3, 5, 6, 7, 8, 9]))        # Output: 4
print(find_missing_ap([-5, -2, 1, 4, 7, 10, 16]))    # Output: 13
