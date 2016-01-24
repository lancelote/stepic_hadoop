# coding=utf-8

""""
Реализуйте reducer в задаче подсчета среднего времени, проведенного
пользователем на странице.

Mapper передает в reducer данные в виде key / value, где key - адрес страницы,
value - число секунд, проведенных пользователем на данной странице.

Среднее время на выходе приведите к целому числу.

Sample Input:

    www.facebook.com	100
    www.google.com	10
    www.google.com	5
    www.google.com	15
    stepic.org	60
    stepic.org	100

Sample Output:

    www.facebook.com	100
    www.google.com	10
    stepic.org	80
"""

import sys

prev = ''
time_spent = 0
people = 0

for line in sys.stdin:
    site, time = line.strip().split("\t")
    if prev == '':
        prev = site
    if site != prev:
        print('%s\t%d' % (prev, time_spent/people))
        time_spent = int(time)
        people = 1
        prev = site
    else:
        time_spent += int(time)
        people += 1

if prev:
    print('%s\t%d' % (prev, time_spent/people))
