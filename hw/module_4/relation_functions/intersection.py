# coding=utf-8

""""
Напишите reducer, который делает пересечение элементов из множества A и B.
На вход в reducer приходят пары key / value, где key - элемент множества,
value - маркер множества (A или B)

Sample Input:

    1	A
    2	A
    2	B
    3	B

Sample Output:

    2
"""

import sys

prev = ''

for line in sys.stdin:
    key, value = line.strip().split('\t')

    if key == prev:
        print(prev)
    else:
        prev = key
