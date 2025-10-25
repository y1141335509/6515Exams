import dc


def FriendlyCompetition(A: list[int]) -> int:
    def merge_sort_count(subarr: list[int]) -> tuple[int, int]:
        if len(subarr) <= 1:
            return subarr, 0
        mid = len(subarr) // 2
        left, left_count = merge_sort_count(subarr[:mid])
        right, right_count = merge_sort_count(subarr[mid:])
        merged, merge_count = merge_and_count(left, right)
        return merged, left_count + right_count + merge_count
    
    def merge_and_count(left: list[int], right: list[int]) -> tuple[list[int], int]:
        count = 0
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                count += len(right) - j
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged, count
    _, total_count = merge_sort_count(A)
    return total_count

if __name__ == "__main__":
    A = [1, 3, 2, 5, 4]
    result = FriendlyCompetition(A)
    print(f"Total number of inversions in {A} is: {result}")
    dc.run(FriendlyCompetition, A)
