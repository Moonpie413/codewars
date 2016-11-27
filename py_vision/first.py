# -*- coding: utf-8 -*-
""" test """
from functools import reduce
from collections import Iterable

def sumnum(num):
    """ hello test """
    return reduce(lambda x, y: x + y, list(range(1, num + 1)))

def dictiter(dic):
    " diciter test "
    if isinstance(dic, Iterable):
        for item in dic.items():
            print(item)

def multitable():
    """ 无聊打下乘法口诀表 """
    print([str(y) + '*' + str(x) + '=' + str(x*y) for x in range(1, 10) for y in range(1, x + 1)])

def triangles():
    """ 杨辉三角 """
    lis = [1]
    while True:
        yield lis
        lis = [1] + [lis[i - 1] + lis[i] for i in range(len(lis))[1:]] + [1]

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

