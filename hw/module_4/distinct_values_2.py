# coding=utf-8

""""
Реализуйте reducer из фазы 1 задачи Distinct Values v1.

Reducer принимает на вход данные, созданные mapper из предыдущей шага.

Sample Input:

    1,a	1
    1,b	1
    1,b	1
    2,a	1
    2,d	1
    2,e	1
    3,a	1
    3,b	1

Sample Output:

    1,a
    1,b
    2,a
    2,d
    2,e
    3,a
    3,b
"""

import sys

previous_value = ''
categories_seen = []

for line in sys.stdin:
    record, count = line.strip().split('\t')
    value, category = record.split(',')

    # First input line
    if not previous_value:
        previous_value = value
        categories_seen.append(category)
        print('%s,%s' % (value, category))

    # Value did not changed
    if value == previous_value:
        if category not in categories_seen:
            categories_seen.append(category)
            print('%s,%s' % (value, category))

    # New value
    else:
        previous_value = value
        categories_seen = [category]
        print('%s,%s' % (value, category))
