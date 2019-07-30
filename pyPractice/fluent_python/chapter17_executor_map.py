# -*- coding:utf-8 -*-
from concurrent import futures
from time import sleep,strftime




def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done'
    display(msg.format('\t'*n,n))
    return n * 10

def main():
    display('script starting')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, [5,3,2,1,9])
    display('results:', results)
    display('Waiting for individual result:')
    for i , result in enumerate(results):
        display('result{}:{}'.format(i, result))

main()