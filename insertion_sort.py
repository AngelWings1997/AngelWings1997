# 插入排序

def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and cur < arr[pre_index]:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = cur
    return arr


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", insertion_sort(arr))