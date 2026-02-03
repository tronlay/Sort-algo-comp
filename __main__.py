import sys
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import các module thuật toán và data generator
# (Giả sử bạn đã tổ chức thư mục như các bước trước: sorting/ và data_generator.py)
from algo import quick_sort, heap_sort, merge_sort, numpy_sort
from data_generator import DataGen

# Tăng giới hạn đệ quy cho QuickSort/MergeSort với dữ liệu lớn
sys.setrecursionlimit(10**6)

class BenchmarkRunner:
    def __init__(self, data_size=1_000_000):
        # Lưu ý: 1e6 phần tử với Python thuần (Quick/Merge) sẽ rất chậm hoặc tràn bộ nhớ.
        # Để demo chạy mượt, mình để mặc định 100k. Bạn có thể sửa thành 1_000_000.
        self.data_size = data_size
        self.gen = DataGen(size=data_size)
        self.results = []
        
        # Danh sách thuật toán cần test
        self.algorithms = [
            ("Quick Sort", quick_sort),
            ("Heap Sort", heap_sort),
            ("Merge Sort", merge_sort),
            ("NumPy Sort", numpy_sort)
        ]

    def _measure_time(self, algo_name, func, data):
        """Hàm đo thời gian chạy đơn lẻ, có xử lý lỗi StackOverflow"""
        # Quan trọng: Phải copy data để không làm hỏng dữ liệu gốc cho thuật toán sau
        if algo_name == "NumPy Sort":
            arr = data.copy()
        else:
            arr = data.tolist() # Chuyển về list python cho các algo tự viết

        try:
            start_time = time.time()
            func(arr)
            return time.time() - start_time
        except RecursionError:
            print(f"   [!] {algo_name} bị lỗi đệ quy (Stack Overflow)!")
            return None # Trả về None nếu lỗi
        except Exception as e:
            print(f"   [!] {algo_name} lỗi: {e}")
            return None

    def run_benchmark(self):
        print(f"=== BẮT ĐẦU BENCHMARK (Size: {self.data_size}) ===")
        
        # 1. Sorted Data
        print("\n>> 1. Chạy dữ liệu Tăng dần (Sorted)...")
        data_sorted = self.gen.get_sorted_float()
        self._run_scenario("Sorted (Best Case)", [data_sorted])

        # 2. Reverse Data
        print("\n>> 2. Chạy dữ liệu Giảm dần (Reverse)...")
        data_reverse = self.gen.get_reverse_float()
        self._run_scenario("Reverse (Worst Case)", [data_reverse])

        # 3. Random Float (5 arrays)
        print("\n>> 3. Chạy 5 mảng Số thực ngẫu nhiên...")
        list_floats = self.gen.get_random_floats(5)
        self._run_scenario("Random Float (Avg 5 runs)", list_floats)

        # 4. Random Int (5 arrays)
        print("\n>> 4. Chạy 5 mảng Số nguyên ngẫu nhiên...")
        list_ints = self.gen.get_random_ints(5)
        self._run_scenario("Random Int (Avg 5 runs)", list_ints)

    def _run_scenario(self, scenario_name, data_list):
        """Chạy một kịch bản (có thể gồm 1 hoặc nhiều mảng data)"""
        for algo_name, func in self.algorithms:
            total_time = 0
            valid_runs = 0
            
            # QuickSort thường chết ở Sorted/Reverse lớn, ta sẽ skip nếu cần thiết
            # hoặc để nó chạy và catch lỗi trong _measure_time
            
            print(f"   -> Testing {algo_name}...", end="", flush=True)
            
            for data in data_list:
                t = self._measure_time(algo_name, func, data)
                if t is not None:
                    total_time += t
                    valid_runs += 1
            
            if valid_runs > 0:
                avg_time = total_time / valid_runs
                print(f" {avg_time:.4f}s")
                self.results.append({
                    "Scenario": scenario_name,
                    "Algorithm": algo_name,
                    "Time (s)": avg_time
                })
            else:
                print(" Failed.")
                self.results.append({
                    "Scenario": scenario_name,
                    "Algorithm": algo_name,
                    "Time (s)": 0 # Đánh dấu 0 hoặc NaN
                })

    def show_statistics(self):
        """Tạo bảng thống kê bằng Pandas"""
        df = pd.DataFrame(self.results)
        
        # Pivot table để nhìn rõ hơn: Hàng = Scenario, Cột = Algorithm
        pivot_df = df.pivot(index="Scenario", columns="Algorithm", values="Time (s)")
        
        print("\n" + "="*50)
        print("BẢNG THỐNG KÊ TỐC ĐỘ (Giây)")
        print("="*50)
        print(pivot_df)
        print("="*50)
        
        return pivot_df

    def plot_chart(self, df):
        """Vẽ biểu đồ cột"""
        print("\n>> Đang vẽ biểu đồ...")
        
        # Plot
        ax = df.plot(kind='bar', figsize=(12, 6), width=0.8)
        
        plt.title(f'So sánh tốc độ các thuật toán sắp xếp (Data Size: {self.data_size})', fontsize=16)
        plt.ylabel('Thời gian chạy (Giây)', fontsize=12)
        plt.xlabel('Loại dữ liệu', fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend(title="Thuật toán")
        
        # Hiển thị giá trị trên đầu cột
        for p in ax.patches:
            if p.get_height() > 0:
                ax.annotate(f'{p.get_height():.2f}', 
                            (p.get_x() + p.get_width() / 2., p.get_height()), 
                            ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # KHUYẾN NGHỊ: Chạy test với 10,000 hoặc 100,000 trước. 
    # Nếu máy mạnh và chấp nhận chờ lâu thì đổi thành 1_000_000.
    runner = BenchmarkRunner(data_size=1_000_000) 
    
    runner.run_benchmark()
    stats_df = runner.show_statistics()
    runner.plot_chart(stats_df)
