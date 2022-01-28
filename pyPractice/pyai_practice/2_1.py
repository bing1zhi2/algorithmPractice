# -*- coding:utf-8 -*-

def isprime(number:int):
    isprime = True
    try:
        for i in range(2,number):
            if number % i == 0:
                isprime = False
                break
    
    except TypeError as e:
        isprime = False
    return isprime


print(isprime(6))


    