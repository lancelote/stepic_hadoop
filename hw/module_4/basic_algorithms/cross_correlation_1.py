# coding=utf-8

""""
Реализуйте mapper для задачи Cross-Correlation, который для каждого кортежа
создает все пары элементов, входящих в него.

Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных
пробелом.

Mapper пишет данные в виде key / value, где key - пара объектов, разделенных
запятой, value - единица.

Sample Input:

    a b
    a b a c

Sample Output:

    a,b	1
    b,a	1
    a,b	1
    a,c	1
    b,a	1
    b,a	1
    b,c	1
    a,b	1
    a,c	1
    c,a	1
    c,b	1
    c,a	1
"""

import sys

for line in sys.stdin:
    items = line.strip().split()
    for i in items:
        for j in items:
            if i != j:
                print('%s,%s\t1' % (i, j))
