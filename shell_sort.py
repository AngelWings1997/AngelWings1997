# 希尔排序
# coding=utf-8
# https://zhuanlan.zhihu.com/p/141822073
# https://www.cnblogs.com/pythonbao/p/10793487.html

def shell_sort(arr):
    """
    希尔排序
    :param arr: 待排序的List
    :return: 希尔排序是就地排序(in-place)
    """
    length = len(arr)
    # 取整计算增量（间隔）值
    gap = length // 2

    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, length):
            cur = arr[i]
            j = i
            # 元素与其同列的前面的每个元素比较，如果比前面的小则互换
            while j >= gap and cur < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = cur
        # 缩小增量（间隔）值
        gap //= 2

    return arr


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", shell_sort(arr))