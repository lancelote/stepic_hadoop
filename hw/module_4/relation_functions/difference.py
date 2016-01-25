# coding=utf-8

""""
Напишите reducer, который делает вычитание элементов множества B из
множества A. На вход в reducer приходят пары key / value, где key - элемент
множества, value - маркер множества (A или B)

Sample Input:

    1	A
    2	A
    2	B
    3	B

Sample Output:

    1
"""

import sys

key, value = '', ''
prev_key, prev_value = '', ''

for line in sys.stdin:
    key, value = line.strip().split('\t')

    if not prev_key:
        prev_key = key
        prev_value = value
        continue

    if value == 'A' and prev_value == 'A':
        print(prev_key)
    elif value == 'B' and prev_value == 'A' and key != prev_key:
        print(prev_key)

    prev_value = value
    prev_key = key

if value == 'A':
    print(key)
