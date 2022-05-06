# 基数排序

def radix_sort(arr):
    """
    基数排序，数组元素必须是正整数
    LSD模式，从低位到高位
    MSD模式，从高位到低位
    这里是LSD模式
    """
    # 遍历数组获取数组最大值和最大值对应的位数
    max_value = max(arr)
    # 迭代次数，取决于最大值的位数
    iter_count = len(str(max_value))
    for i in range(iter_count):
        # 定义桶，大小为10，对应0 - 9
        bucket = [[] for _ in range(10)]
        for n in arr:
            index = (n // (10 ** i)) % 10
            # bucket[index].append(n)
            bucket[index] += [n]
        # arr数组清零，并合并桶内元素至arr数组
        arr = []
        for num in bucket:
            # arr.extend(num)
            arr += num
    return arr


if __name__ == '__main__':
    import random

    # random.seed(54)
    arr = [random.randint(0, 1000) for _ in range(20)]
    print("原始数据：", arr)
    print("排序结果：", radix_sort(arr))