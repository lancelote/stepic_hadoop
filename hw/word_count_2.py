# coding=utf-8

""""
Напишите программу, которая реализует In-mapper combining v.2 для задачи
WordCount в Hadoop Streaming.

Sample Input:

    aut Caesar aut nihil
    aut aut
    de mortuis aut bene aut nihil

Sample Output:

    aut	6
    mortuis	1
    bene	1
    Caesar	1
    de	1
    nihil	2
"""

import sys
from collections import defaultdict

dct = defaultdict(int)

for line in sys.stdin:
    for word in line.strip().split(" "):
        dct[word] += 1

for word in dct.keys():
    print('%s\t%d' % (word, dct[word]))
