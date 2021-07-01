import numpy as np

# l1 = [1, 2, 3, 4, 5]
#
#
# def squ(x):
#     return x ** 2
#
#
# res = list(map(squ, l1))
#
# l = [i for i in list(map(lambda x: x ** 2, l1)) if i > 10]
#
#
# for j in (i for i in list(map(lambda x: x ** 2, l1)) if i > 10):
#     print(j)



for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %2d ' %( i, j, i * j))
