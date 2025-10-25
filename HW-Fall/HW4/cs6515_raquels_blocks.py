def RaquelsBlocks(blue: list[int], red: list[int]) -> int:
    m, n = len(blue), len(red)
    total = m + n
    
    k = (total - 1) // 2
    
    return find_kth_smallest(blue, red, k)


def find_kth_smallest(blue_blocks, red_blocks, k):
    m, n = len(blue_blocks), len(red_blocks)
    
    red_ascending = red_blocks[::-1]
    
    return find_kth_in_ascending_arrays(blue_blocks, red_ascending, k)


def find_kth_in_ascending_arrays(arr1, arr2, k):
    m, n = len(arr1), len(arr2)
    
    if m > n:
        return find_kth_in_ascending_arrays(arr2, arr1, k)
    
    low = max(0, k - n + 1)  
    high = min(k + 1, m)     
    
    while low <= high:
        count1 = (low + high) // 2
        count2 = k + 1 - count1
        
        # Get boundary elements for comparison
        # Handle edge cases with -infinity and +infinity
        left1 = arr1[count1 - 1] if count1 > 0 else float('-inf')
        right1 = arr1[count1] if count1 < m else float('inf')
        
        left2 = arr2[count2 - 1] if count2 > 0 else float('-inf')
        right2 = arr2[count2] if count2 < n else float('inf')
        
        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        elif left1 > right2:
            high = count1 - 1
        else:
            low = count1 + 1
    
    raise ValueError("No valid partition found")
