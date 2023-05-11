import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([], -1, "test"), "Индекс должен быть неотрицательным числом!")
        self.assertEqual(arrs.get([1, "3", 5], "1", "test"), "Индекс должен быть целым числом! ")
        self.assertEqual(arrs.get(["tested", "3", 5], 1, "test"), "3")
        self.assertEqual(arrs.get("testing", 1, "test"), "Данные должны быть в формате списка!")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1), [2, 3, 4])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, 3), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
