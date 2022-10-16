import random


def readfile():
    f = open('numbers.txt', 'w')
    for i in range((10 ** 6)):
        f.write(str(random.randint(-1000, 1000)))
        f.write(' ')
    with open('numbers.txt', 'r') as f:
        num = f.readline().split(' ')


def _min(num):
    result = num[0]
    for i in num:
        if result > i:
            result = i
    return result


def _max(num):
    result = num[0]
    for i in num:
        if result < i:
            result = i
    return result


def _sum(num):
    result = 0
    for i in num:
        result += i
    return result


def _mult(num):
    result = 1
    for i in num:
        result *= i
    return result

