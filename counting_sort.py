# 计数排序

def counting_sort(arr):
    # 获取最大，最小值
    largest = max(arr)
    smallest = min(arr)
    # 用于统计个数的空数组
    counter = [0 for _ in range(largest - smallest + 1)]
    # 桶内索引值
    idx = 0
    for i in range(len(arr)):
        # 统计每个元素出现的次数
        counter[arr[i] - smallest] += 1
    for j in range(len(counter)):
        while counter[j] > 0:
            # 取出元素
            arr[idx] = j + smallest
            idx += 1
            # 对应桶的计数器减1
            counter[j] -= 1
    return arr


if __name__ == '__main__':
    import random

    # random.seed(54)
    arr = [random.randint(0, 1000) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", counting_sort(arr))