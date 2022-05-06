# 快速排序

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


'''
def quick_sort(arr):    
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