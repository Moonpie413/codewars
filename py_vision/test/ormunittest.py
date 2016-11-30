# -*-coding:utf-8 -*-
' a unit test for model '

import unittest
import myorm

class ModelTest(unittest.TestCase):
    'a simple test for orm'

    def setUp(self):
        self.sdict = myorm.Model()
        self.user = myorm.User(uid='1234', name='xiaoli')

    def test_dict(self):
        ' test key equal value or not '
        self.sdict['key'] = 'value'
        self.assertEqual(self.sdict.key, 'value')

    def test_save(self):
        ' a save test '
        self.user.save()
