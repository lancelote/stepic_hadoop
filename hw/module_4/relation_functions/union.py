# coding=utf-8

""""
Напишите reducer, который объединяет элементы из множества A и B.
На вход в reducer приходят пары key / value, где key - элемент множества,
value - маркер множества (A или B)

Sample Input:

    1	A
    2	A
    2	B
    3	B

Sample Output:

    1
    2
    3
"""

import sys

prev = ''

for line in sys.stdin:
    key, value = line.strip().split('\t')

    # First line
    if not prev:
        print(key)
        prev = key

    # First key occurrence
    elif key != prev:
        print(key)
        prev = key
