from algorithms import bubble_sort, quick_sort, merge_sort

def main():
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数据: {test_data}")
    
    print(f"冒泡排序: {bubble_sort(test_data)}")
    print(f"快速排序: {quick_sort(test_data)}")
    print(f"归并排序: {merge_sort(test_data)}")

if __name__ == "__main__":
    main()
