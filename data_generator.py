import numpy as np

class DataGen:
    """
    Module sinh dữ liệu test cho các thuật toán sắp xếp.
    Dữ liệu được sinh bằng NumPy để tối ưu tốc độ và trả về dưới dạng NumPy Array.
    """
    
    def __init__(self, size=1_000_000, max_val=1_000_000_000):
        self.size = size
        self.max_val = max_val

    def get_sorted_float(self):
        """1. Tạo 1 dãy số thực tăng dần"""
        print(f"[DataGen] Đang sinh {self.size} số thực tăng dần...")
        # Tạo ngẫu nhiên rồi sort
        arr = np.random.uniform(0, self.max_val, self.size)
        arr.sort()
        return arr

    def get_reverse_float(self):
        """2. Tạo 1 dãy số thực giảm dần"""
        print(f"[DataGen] Đang sinh {self.size} số thực giảm dần...")
        # Tạo ngẫu nhiên, sort, rồi đảo ngược
        arr = np.random.uniform(0, self.max_val, self.size)
        # np.sort trả về tăng dần, [::-1] để đảo ngược
        return np.sort(arr)[::-1]

    def get_random_floats(self, num_arrays=5):
        """3. Tạo 5 dãy số thực ngẫu nhiên. Trả về list chứa 5 arrays."""
        print(f"[DataGen] Đang sinh {num_arrays} dãy số thực ngẫu nhiên...")
        data_list = []
        for i in range(num_arrays):
            arr = np.random.uniform(0, self.max_val, self.size)
            data_list.append(arr)
        return data_list

    def get_random_ints(self, num_arrays=5):
        """4. Tạo 5 dãy số nguyên ngẫu nhiên. Trả về list chứa 5 arrays."""
        print(f"[DataGen] Đang sinh {num_arrays} dãy số nguyên ngẫu nhiên...")
        data_list = []
        for i in range(num_arrays):
            # Dùng randint cho số nguyên
            arr = np.random.randint(0, self.max_val, self.size)
            data_list.append(arr)
        return data_list
