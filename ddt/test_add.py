import unittest


# 加法操作
def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):

    def test_add1(self):
        result = add(1, 1)
        print("result=", result)
        self.assertEqual(2, result)

    def test_add2(self):
        result = add(1, 0)
        print("result=", result)
        self.assertEqual(1, result)

    def test_add3(self):
        result = add(0, 0)
        print("result=", result)
        self.assertEqual(0, result)
