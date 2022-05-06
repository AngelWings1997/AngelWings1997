# 选择排序

def selection_sort(arr):
    for i in range(0, len(arr)):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", selection_sort(arr))