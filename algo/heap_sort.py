from typing import List

def _heapify(arr: List[int], n: int, i: int):
    """Hàm helper (private) để vun đống"""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def sort(arr: List[int]) -> List[int]:
    """
    Thực hiện HeapSort.
    Time Complexity: O(n log n).
    """
    n = len(arr)
    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    
    return arr