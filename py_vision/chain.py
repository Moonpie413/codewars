# -*-coding:utf-8 -*-
' test for chain '

class Chain(object):
    ' A class to test chain '
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def users(self, user):
        ' users '
        return Chain('/users/:%s' % user)

    def __str__(self):
        return self.__path

    __repr__ = __str__

class UpperAttrMetaclass(type):
    ' metaclass test '
    def __new__(mcs, names, bases, dct):
        return type.__new__(mcs, names, bases,
                            dict((name.upper(), value)
                                 for name, value in dct.items() if not name.startswith('__')))

class MetaedClass(metaclass=UpperAttrMetaclass):
    ' MetaedClass '
    mname = 'mname'

print(Chain().users('xiaoming').repo)
print(hasattr(MetaedClass, 'MNAME'))
