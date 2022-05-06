# 归并排序

# 方法一：自上而下的递归
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    """
    入参数组都是有序的，此处将两个有序数组合并成一个大的有序数组
    """
    # 两个数组的起始下标
    l, r = 0, 0

    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            # result.append(left[l])
            result += [left[l]]
            l += 1
        else:
            # result.append(right[r])
            result += [right[r]]
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", merge_sort(arr))
