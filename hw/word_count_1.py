# coding=utf-8

""""
Напишите программу, которая реализует In-mapper combining v.1 для задачи
WordCount в Hadoop Streaming.

Sample Input:

    aut Caesar aut nihil
    aut aut
    de mortuis aut bene aut nihil

Sample Output:

    nihil	1
    aut	2
    Caesar	1
    aut	2
    nihil	1
    aut	2
    de	1
    bene	1
    mortuis	1
"""

import sys
from collections import defaultdict

for line in sys.stdin:
    dct = defaultdict(int)
    for word in line.strip().split(" "):
        dct[word] += 1
    for word in dct.keys():
        print('%s\t%d' % (word, dct[word]))
