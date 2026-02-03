from typing import List

def sort(arr: List[int]) -> List[int]:
    """
    Thực hiện MergeSort.
    Time Complexity: O(n log n).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        sort(L)
        sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking left elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Checking right elements
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr