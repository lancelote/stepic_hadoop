# coding=utf-8

""""
Реализуйте mapper из фазы 1 задачи Distinct Values v1.

Mapper принимает на вход строку, содержащую значение и через табуляцию список
групп, разделенных запятой.

Sample Input:

    1	a,b
    2	a,d,e
    1	b
    3	a,b

Sample Output:

    1,a	1
    1,b	1
    2,a	1
    2,d	1
    2,e	1
    1,b	1
    3,a	1
    3,b	1
"""

import sys

for line in sys.stdin:
    value, categories = line.strip().split('\t')
    category_list = categories.split(',')

    for category in category_list:
        print('%s,%s\t1' % (value, category))
