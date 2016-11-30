# -*-coding:utf-8 -*-
'''
a simple metaclass based orm frarmwork
一个简易的python实现的orm框架
利用metaclass在创建对象前将对象中的属性添加到一个mapping中
创建完对象后再调用save方法把之前的mapping转化为字符串输出，这里只实现了打印，有了sql语句就可以实现更复杂的功能
'''

class Field(object):
    ' Field based class '
    def __init__(self, name, colum_name):
        self.__name = name
        self.__colum_name = colum_name

    @property
    def name(self):
        ' getter of name '
        return self.__name

    @property
    def colum_name(self):
        ' getter of colum_name '
        return self.__colum_name


    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__, self.__name)

class StringFiled(Field):
    ' String type of Field '
    def __init__(self, name, length):
        super(StringFiled, self).__init__(name, 'varchar(' + length.__str__() + ')')

class IntegerField(Field):
    ' Integer type of Field '
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    ' model obj creater AKA custom type class '
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            return super(ModelMetaclass, mcs).__new__(mcs, name, bases, attrs)
        print('Found Model: %s' % name)
        mapping = dict()
        for key, value in attrs.items():
            if isinstance(value, Field):
                print('Found mapping: %s' % value)
                mapping[key] = value
        for key in mapping:
            attrs.pop(key)
        attrs['__mapping__'] = mapping
        attrs['__table__'] = name.upper()
        return super(ModelMetaclass, mcs).__new__(mcs, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    ' custom model class '
    def __init__(self, **kw):
        super(Model, self).__init__(kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            print('ERROR! %s has no attribute %s!' % (self.__class__.__name__, key))
            return None

    def __setattr__(self, key, value):
        self[key] = value

    def __str__(self):
        return super(Model, self).__str__()

    def save(self):
        ' convert user model to a sql string '
        field_names = []
        args = []
        for key, value in self.__mapping__.items():
            arg = getattr(self, key)
            if arg:
                field_names.append(value.name)
                # getattr 用来从对象中取出name对应的value
                args.append(arg)
        sql = 'INSERT INTO %s (%s) values (%s)' % (
            self.__table__,
            ','.join(field_names),
            ','.join(list(map(lambda x: '?', [x for x in range(field_names.__len__())]))))
        print('SQL: %s' % sql)
        print('args: %s' % args)

class User(Model):
    ' test user model '
    uid = IntegerField('uid')
    name = StringFiled('name', 20)
    email = StringFiled('email', 20)



