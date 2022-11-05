from math import *
from decimal import *
def decimal_to_binary(num):
    if num != type(float()) : num = float(num)
    num = list(modf(num))
    if num[0] == 0 and num[1] == 0 : return '0'
    negative = num[1] < 0
    num[1] = abs(int(num[1]))
    zero = num[1]
    remainder = ""
    while num[1]!=0:
        remainder = str(num[1]%2) + remainder
        num[1] //= 2
    if num[0] != 0:
        num[0] = abs(num[0])
        if zero == 0:
            remainder += "0."
        else:
            remainder += "."
        i = 0
        while num[0] != 0:
            if i == 20 : break
            num[0] *= 2
            remainder += str(int(modf(num[0])[1]))
            num[0] = modf(num[0])[0]
            i += 1
    return '-' + remainder if negative else remainder
def decimal_to_octal(num):
    if num != type(float()) : num = float(num)
    num = list(modf(num))
    if num[0] == 0 and num[1] == 0 : return '0'
    negative = num[1] < 0
    num[1] = abs(int(num[1]))
    zero = num[1]
    remainder = ""
    while num[1]!=0:
        remainder = str(num[1]%8) + remainder
        num[1] //= 8
    if num[0] != 0:
        num[0] = abs(num[0])
        if zero == 0:
            remainder += "0."
        else:
            remainder += "."
        i = 0
        while num[0] != 0:
            if i == 20 : break
            num[0] *= 8
            remainder += str(int(modf(num[0])[1]))
            num[0] = modf(num[0])[0]
            i += 1
    return '-' + remainder if negative else remainder
def decimal_to_BCD(num):
    num = f'{num}'
    result = ''
    for i in num:
        temp = decimal_to_binary(i)
        result += ((4 - len(temp)) * '0') + temp
    return result
