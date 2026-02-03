import numpy as np
from typing import List

def sort(arr: List[int]) -> List[int]:
    """
    Wrapper gọi hàm sort của NumPy.
    Chuyển đổi list -> numpy array -> list để đồng bộ output.
    """
    np_arr = np.array(arr)
    sorted_np = np.sort(np_arr)
    return sorted_np.tolist()