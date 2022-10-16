import matplotlib.pyplot as plt
import time
import random
import sys

num = []


def _min():
    min_num = sys.maxsize
    for i in num:
        if min_num > i:
            min_num = i
        min_num = min(i, min_num)
    return min_num


sz = 0
x = list(range(0, 200))
y = []
for i in range(0, 200):
    n = sz
    time_start = time.time()
    num.clear()
    for i in range(0, sz):
        num.append(random.randint(-1000, 1000))
    sz += 100
    _min()
    y.append(time.time() - time_start)
plt.plot(x, y)
plt.show()
