import unittest
from parameterized import parameterized


# 加法操作
def add(x, y):
    return x + y


def build_data():
    return [(1, 1, 2), (1, 0, 1), (0, 0, 0)]


class TestAdd(unittest.TestCase):

    # def test_add1(self):
    #     result = add(1, 1)
    #     print("result=", result)
    #     self.assertEqual(2, result)
    #
    # def test_add2(self):
    #     result = add(1, 0)
    #     print("result=", result)
    #     self.assertEqual(1, result)
    #
    # def test_add3(self):
    #     result = add(0, 0)
    #     print("result=", result)
    #     self.assertEqual(0, result)

    # @parameterized.expand([(1, 1, 2), (1, 0, 1), (0, 0, 0)])
    @parameterized.expand(build_data)
    def test_add(self, x, y, expect):
        print("x={} y={} expect={}".format(x, y, expect))
        result = add(x, y)
        print("result=", result)
        self.assertEqual(expect, result)
