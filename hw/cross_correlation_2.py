# coding=utf-8

""""
Реализуйте mapper для задачи Cross-Correlation, который для каждого объекта из
кортежа создает stripe.

Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных
пробелом.

Mapper пишет данные в виде key / value, где key - объект, value -
соответствующий stripe (пример: a:1,b:2,c:3)

Sample Input:

    a b
    a b a c

Sample Output:

    a	b:1
    b	a:1
    a	b:1,c:1
    b	a:2,c:1
    a	b:1,c:1
    c	b:1,a:2
"""

import sys
from collections import defaultdict


def stripe_to_str(dct):
    result = []
    for element in dct.keys():
        result.append(element + ':' + str(dct[element]))
    return ','.join(result)

for line in sys.stdin:
    items = line.strip().split()
    for i in items:
        stripe = defaultdict(int)

        for j in items:
            if i != j:
                stripe[j] += 1

        print('%s\t%s' % (i, stripe_to_str(stripe)))
