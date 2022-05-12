# 快速排序
"""
:cvar: 快速排序算法步骤：
    1. 从数列中挑出一个元素，称为 "基准"（pivot）;
    2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就
    处于数列的中间位置。这个称为分区（partition）操作；
    3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
"""


def quick_sort(arr):
    """
    快速排序，平均时间复杂度: O(nlog2n)，最好情况: O(nlog2n)，最坏情况: O(n^2)，空间复杂度: O(log2n)，排序方式: in-place，不稳定（不稳
    定算法还有选择排序，希尔排序和堆排序）。
    使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists），是一种分而治之思想在排序算法上的典型应用。本质上来
    看，算是在冒泡排序基础上的递归分治法。
    在大多数情况下都比平均时间复杂度为 O(nlog2n) 的排序算法表现要更好，快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时
    间是 O(nlog2n)，且 O(nlog2n) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlog2n) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机
    数列而言，快速排序总是优于归并排序。
    注意nlog2n，其中2表示以2为底。可选择不同的 "基准"（pivot），这里我们选择第一个元素作为基准。
    :param arr: List[int]
    :return: 升序排列的 List[int]
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


'''
def quick_sort(arr):  
    """
    快速排序，平均时间复杂度: O(nlog2n)，最好情况: O(nlog2n)，最坏情况: O(n^2)，空间复杂度: O(log2n)，排序方式: in-place，不稳定（不稳
    定算法还有选择排序，希尔排序和堆排序）。
    使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists），是一种分而治之思想在排序算法上的典型应用。本质上来
    看，算是在冒泡排序基础上的递归分治法。
    在大多数情况下都比平均时间复杂度为 O(nlog2n) 的排序算法表现要更好，快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时
    间是 O(nlog2n)，且 O(nlog2n) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlog2n) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机
    数列而言，快速排序总是优于归并排序。
    注意nlog2n，其中2表示以2为底。可选择不同的 "基准"（pivot），这里我们选择中间的元素 (len(arr) // 2) 作为基准。
    :param arr: List[int]
    :return: 升序排列的 List[int]
    """  
    if len(arr) < 2:        
        return arr 
   
    pivot = arr[len(arr) // 2]    
    left = [x for x in arr if x < pivot]    
    middle = [x for x in arr if x == pivot]    
    right = [x for x in arr if x > pivot]    
    return quick_sort(left) + middle + quick_sort(right)
'''


if __name__ == '__main__':
    import random

    # random.seed(54)
    arr = [random.randint(0, 1000) for _ in range(10)]
    print("原始数据：", arr)
    print("排序结果：", quick_sort(arr))