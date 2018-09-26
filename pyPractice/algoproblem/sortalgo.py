# -*- coding:utf-8 -*-


def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = tmp
    return a


b = insertion_sort([5, 2, 9, 3])
print(b)
