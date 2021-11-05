import unittest

from sock_merchant import matchingSocks

class SockTest(unittest.TestCase):

    def test_array1(self):
        number = 30
        array = [2, 3, 299, 1, 5, 6, 6, 3, 3, 9, 8, 90, 7, 0, 1, 0, 2, 4, 5, 4, 4, 5, 6, 6, 10, 9, 27, 28, 27, 30]
        result = matchingSocks(number, array)
        self.assertEqual(result, 10)

    def test_array2(self):
        number = 80
        array = [2, 3, 299, 1, 5, 6, 6, 3, 3, 9, 8, 90, 7, 0, 1, 0, 2, 4, 5, 4, 4, 5, 6, 6, 10, 9, 27, 28, 27, 30, 2, 3, 299, 1, 5, 6, 6, 3, 3, 9, 8, 90, 7, 0, 1, 0, 2, 4, 5, 4, 4, 5, 6, 6, 10, 9, 27, 28, 27, 30, 2, 3, 299, 1, 5, 6, 6, 3, 3, 9, 8, 90, 7, 0, 1, 0, 2, 4, 5]
        result = matchingSocks(number, array)
        self.assertEqual(result, 36)

if __name__ == '__main__':
    unittest.main()