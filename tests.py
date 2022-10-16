import unittest
import math
import time
from functions import _min, _max, _sum, _mult, readfile

readfile()
num = [int(i) for i in open('numbers.txt', 'r').readline().split()]


class Test(unittest.TestCase):

    def test_min(self):
        start = time.time()
        self.assertEqual(_min(num), min(num))
        print('test_min duration: ', time.time() - start)

    def test_max(self):
        start = time.time()
        self.assertEqual(_max(num), max(num))
        print('test_max duration: ', time.time() - start)

    def test_sum(self):
        start = time.time()
        self.assertEqual(_sum(num), sum(num))
        print('test_sum duration: ', time.time() - start)

    def test_mult(self):
        start = time.time()
        self.assertEqual(_mult(num), math.prod(num))
        print('test_mult duration: ', time.time() - start)

    def test_any(self):
        start = time.time()
        self.assertLess(_min(num), _max(num))
        print('test_any duration: ', time.time() - start)


if __name__ == '__main__':
    unittest.main()
