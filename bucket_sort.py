# 桶排序
"""
程序说明：
    桶排序
    1）在额外空间充足的情况下，尽量增大桶的数量
    2）使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
      个人理解，如果都是整数还可以用计数排序来计数统计然后排序，但是如果是一个连续空间内的排序，即统计的是一个浮点类型的数组成
      的数组，那么，就无法开辟一个对应的空间使其一一对应的存储。此时，我们需要新建一个带有存储范围的空间，来存储一定范围内的元素
    空间复杂度：O(n)
    时间复杂度: O(n)
    稳定
"""


def bucket_sort(arr):
    largest = max(arr)
    # 不能使用[[]] * (max + 1)，这样新建的空间中各个[]是共享内存的，导致后面的操作会影响到前面的空间
    buf = {i: [] for i in range(int(largest) + 1)}
    arr_len = len(arr)
    for i in range(arr_len):
        # num = arr[i]
        # 将相应范围内的数据加入到[]中
        # buf[int(num)].append(num)
        buf[int(arr[i])] += [arr[i]]
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            # 这里还需要对一个范围内的数据进行排序，然后再进行输出
            # arr.extend(sorted(buf[i]))
            arr += (sorted(buf[i]))
    return arr


if __name__ == '__main__':
    import random

    # random.seed(54)
    arr = [random.randint(0, 1000) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", bucket_sort(arr))