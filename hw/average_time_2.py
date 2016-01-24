# coding=utf-8

""""
Реализуйте Combiner в задаче подсчета среднего времени, проведенного
пользователем на странице.

Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара
чисел, разделенных ";". Первое - число секунд, проведенных пользователем на
данной странице, второе равно 1.

Sample Input:

    www.facebook.com	100;1
    www.google.com	10;1
    www.google.com	5;1
    www.google.com	15;1
    stepic.org	60;1
    stepic.org	100;1

Sample Output:

    www.facebook.com	100;1
    www.google.com	30;3
    stepic.org	160;2
"""

import sys

prev = ''
time_spent = 0
visits = 0

for line in sys.stdin:
    site, pair = line.strip().split('\t')
    time, n = map(int, pair.split(';'))

    if not prev:
        prev = site

    if site != prev:
        print('%s\t%d;%d' % (prev, time_spent, visits))
        time_spent = time
        visits = 1
        prev = site
    else:
        time_spent += time
        visits += n

if prev:
    print('%s\t%d;%d' % (prev, time_spent, visits))
