# 堆排序

def build_heap(arr, n, i):
    # 构造大顶堆
    large_index = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        large_index = l

    if r < n and arr[large_index] < arr[r]:
        large_index = r

    # 通过上面跟左右节点比较后，得出三个元素之间较大的下标，如果较大下表不是父节点的下标，说明交换后需要重新调整大顶堆
    if large_index != i:
        arr[i], arr[large_index] = arr[large_index], arr[i]
        # large_index位置的数字（也就是最开始输入那个arr[i]）处于待定状态，需要在它所有根部中确定其位置
        build_heap(arr, n, large_index)


def heap_sort(arr):
    length = len(arr)

    # 构造大顶堆
    for i in range(length, -1, -1):
        # 在全堆中逐个调整每个数字的位置，调整的方法是在它所有根部中确定其位置
        build_heap(arr, length, i)

    # 逐个交换元素
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # 把新上来的0号元素安排到合适的位置上去,其中i指的是要调整的堆的范围
        build_heap(arr, i, 0)
    return arr


if __name__ == '__main__':
    import random

    # random.seed(54)
    arr = [random.randint(0, 1000) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", heap_sort(arr))