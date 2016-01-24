# coding=utf-8

""""
Реализуйте reducer из задачи Distinct Values v2.

Reducer принимает на вход строки, каждая из которых состоит из разделенных
табуляцией значения и названия группы.

Sample Input:

    1	a
    1	b
    1	b
    2	a
    2	d
    2	e
    3	a
    3	b

Sample Output:

    a	3
    d	1
    b	2
    e	1
"""

import sys
from collections import defaultdict

categories = defaultdict(int)
categories_seen = []
previous_value = ''

for line in sys.stdin:
    value, category = line.strip().split('\t')

    # First input line
    if not previous_value:
        previous_value = value
        categories_seen.append(category)
        categories[category] += 1

    # Value did not changed
    if value == previous_value:
        if category not in categories_seen:
            categories_seen.append(category)
            categories[category] += 1

    # New value
    else:
        previous_value = value
        categories_seen = [category]
        categories[category] += 1

for category in categories.keys():
    print('%s\t%s' % (category, categories[category]))
