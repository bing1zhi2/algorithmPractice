# -*- coding:utf-8 -*-
# 对truple 和数组进行学习
print('hello word')
b = [('u1', 'A'), ('u1', 'B'), ('u1', 'C'), ('u2', 'B'), ('u2', 'C')]
d = {}


def t2d(t):
    k = t[0]
    value = t[1]
    if k in d:
        li = d[k]
        li.append(value)
        d[k] = li
    else:
        li = [value]
        d[k] = li


for i in range(len(b)):
    print(b[i])
    key = b[i][0]
    t2d(b[i])

print(d)


def gets(d):
    list = []
    for k in d:
        li = d[k]
        pd = []
        for idx in range(len(li)):
            for j in range(idx + 1, len(li)):
                st = li[idx] + '_' + li[j]
                pd.append(st)

        list.append((k, pd))
    return list


print(gets(d))




