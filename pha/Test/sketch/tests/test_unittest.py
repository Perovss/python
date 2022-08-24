import unittest
from main import multiplication_int, multiplication_string

class TestFunction(unittest.TestCase):
    def setUp(self):
        print('=====> setUp')

    def tearDown(self):
        print('=====> tearDown')


    def test_multiplication_int(self):
        '''Это метод тестирования функции multiplication_int'''
        result = multiplication_int(2, 2)
        etalon = 4
        self.assertEqual(result, etalon)
