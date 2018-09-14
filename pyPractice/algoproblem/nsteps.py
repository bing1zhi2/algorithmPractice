# -*- coding:utf-8 -*-


def n_steps(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return n_steps(n - 3) + n_steps(n - 2) + n_steps(n - 1)


print(n_steps(20))
