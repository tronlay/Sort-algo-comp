from typing import List

def sort(arr: List[int]) -> List[int]:
    """
    Thực hiện QuickSort.
    Time Complexity: O(n log n) trung bình.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return sort(left) + middle + sort(right)