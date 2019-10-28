# -*- coding:utf-8 -*-
"""
快速排序
思路：
   1选择一个数做基准
   2划分子集，左边比基准小，右边比基准大。
   3对子集排序，
   4，分治
"""


def median3(arr, left, right):
    """
    选择基准的算法，从左中右三个中选择中位数
    :param arr:
    :param left:
    :param right:
    :return:
    """
    center = (left + right) // 2
    if arr[left] > arr[center]:
        # 交换
        temp = arr[left]
        arr[left] = arr[center]
        arr[center] = temp
    if arr[left] > arr[right]:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
    if arr[center] > arr[right]:
        temp = arr[center]
        arr[center] = arr[right]
        arr[right] = temp

    # 将基准藏到右边
    temp = arr[center]
    arr[center] = arr[right - 1]
    arr[right - 1] = temp
    return arr[right - 1]


def quick_sort(arr, left, right):
    """

    :param arr:
    :param left:
    :param right:
    :return:
    """
    if right-left <=1:
        return
    # 选择主元（基准）
    pivot = median3(arr, left, right)

    low = left
    high = right - 1
    # 将序列中比基准小的移动到左边，大的移动到右边
    while 1:
        # low向右移动，直到arr[low]>pivot
        # high 向左移动 直到arr[high]<pivot
        while 1:
            low += 1
            if arr[low] >= pivot:
                break
        while 1:
            high -= 1
            if arr[high] <= pivot:
                break
        if low < high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
        else:
            break

    # 交换基准到正确的位置
    temp = arr[low]
    arr[low] = arr[right - 1]
    arr[right - 1] = temp

    # 递归解决左边
    quick_sort(arr, left, low - 1)
    # 递归解决右边
    quick_sort(arr, low + 1, right)


def q_sort(arr, n):
    quick_sort(arr, 0, n - 1)


a = [-1, 8, 1, 4,9,6,0,5,2,7,3,11]

q_sort(a, len(a))
print(a)
