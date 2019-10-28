def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp


def shell_sort(arr, n):
    sedgewick = [929, 505, 209, 109, 41, 19, 5, 1, 0]
    si = 0
    while (sedgewick[si] > n):
        si = si + 1

    d = sedgewick[si]

    while d > 0:
        for p in range(d,n):
            temp = arr[p]
            j = p
            while j>=d and a[j-d]>temp:
                a[j]=a[j-d]
                j -= d
            a[j] = temp
        si = si + 1
        d = sedgewick[si]


a = [3, 4, 1, 45, 5, 67]
# insertion_sort(a, len(a))
shell_sort(a, len(a))
print(a)
