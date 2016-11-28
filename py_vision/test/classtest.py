# -*-coding:utf-8 -*-
' another test '

class Student(object):
    'class of student'
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__gender = ''

    def getname(self):
        ' getname '
        return self.__name

    @property
    def gender(self):
        ' gender '
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def __str__(self):
        return self.__name + ', ' + self.__age.__str__()


print(Student('xiaoming', 19).getname())
XIAOMING = Student('xiaoming', 30)
XIAOMING.gender = 'man'
print(XIAOMING)
