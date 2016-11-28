# -*- coding: utf-8 -*-
' first python '
from functools import reduce, wraps
from collections import Iterable

def sumnum(num):
    ' hello test '
    return reduce(lambda x, y: x + y, list(range(1, num + 1)))

def dictiter(dic):
    " diciter test "
    if isinstance(dic, Iterable):
        for item in dic.items():
            print(item)

def multitable():
    ' 乘法口诀表 '
    print([str(y) + '*' + str(x) + '=' + str(x*y) for x in range(1, 10) for y in range(1, x + 1)])

def triangles():
    ' 杨辉三角 '
    lis = [1]
    while True:
        yield lis
        lis = [1] + [lis[i - 1] + lis[i] for i in range(len(lis))[1:]] + [1]

def calc_sums(*args):
    ' 可变参数计算和 '
    return reduce(lambda x, y: x + y, args)

# def log(func):
#     """ log函数 """
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         """ 内部函数, 把原函数包装后返回，调用时返回原函数值 """
#         print('exec: ' + func.__name__)
#         return func(*args, **kw)
#     return wrapper

def log(text):
    ' log函数 '
    def deco(func):
        ' 装饰器 '
        @wraps(func)
        def wrapper(*args, **kw):
            ' wrapper '
            print(text + ': ' + func.__name__)
            return func(*args, **kw)
        return wrapper
    return deco

@log('text')
def ori():
    ' ori function '
    print('原函数')

# print(sumnum(100))
# dictiter({'1':1, '2':2})
# print(list(range(10))[-3:-1])
# multitable()
# N = 0
# for x in triangles():
#     print(x)
#     N = N + 1
#     if N == 10:
#         break
# print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)], key=lambda t: t[1],
#              reverse=True))
# print(calc_sums(1, 2, 3, 4, 5))
# print(log('text')(ori))

