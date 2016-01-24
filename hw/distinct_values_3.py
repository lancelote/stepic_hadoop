# coding=utf-8

""""
Реализуйте mapper из фазы 2 задачи Distinct Values v1.

Mapper принимает на вход строку, содержащую значение и группу, разделенные
запятой.

Sample Input:

    1,a
    2,a
    3,a
    1,b
    3,b
    2,d
    2,e

Sample Output:

    a	1
    a	1
    a	1
    b	1
    b	1
    d	1
    e	1
"""

import sys

for line in sys.stdin:
    value, category = line.strip().split(',')
    print(category + '\t1')
