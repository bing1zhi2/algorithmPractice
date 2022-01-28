# -*- coding:utf-8 -*-

# 最大公约与最小公倍


# 

def max_yue(number1:int, number2:int):
    if number1 < number2:
        temp = number1
        number1 = number2
        number2 = temp

    m=number1;   n=number2; 
    while( m%n !=0):
        r = m % n
        m = n
        n = r 
    
    print("最大公约数：{}".format(n))
    print("最小公倍数：{}".format(number1*number2//n))

    max_yue = n
    min_bei = number1*number2//n 

    return max_yue, min_bei




b = max_yue(49,35)
print(b)