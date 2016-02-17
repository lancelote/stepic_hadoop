# coding=utf-8

"""
Реализуйте reducer в задаче поиска кратчайшего пути с помощью Hadoop Streaming.

Входные и выходные данные: в качестве ключа идет номер вершины, значение
состоит из двух полей, разделенных табуляцией:

Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
Список исходящих вершин (через "," в фигурных скобках).
Пример работы reducer на второй итерации обработки следующего графа:

Sample Input:

    1	0	{2,3,4}
    10	INF	{}
    10	INF	{}
    2	1	{}
    2	1	{5,6}
    3	1	{}
    3	1	{}
    4	1	{}
    4	1	{7,8}
    5	2	{}
    5	INF	{9,10}
    6	2	{}
    6	INF	{}
    7	2	{}
    7	INF	{}
    8	2	{}
    8	INF	{}
    9	INF	{}
    9	INF	{}

Sample Output:

    1	0	{2,3,4}
    10	INF	{}
    2	1	{5,6}
    3	1	{}
    4	1	{7,8}
    5	2	{9,10}
    6	2	{}
    7	2	{}
    8	2	{}
    9	INF	{}
"""

import sys

head_adjoined_nodes = '{}'
head_min_weight = []
prev_head = ''

for line in sys.stdin:
    head, weight, adjoined_nodes = line.strip().split('\t')

    if not prev_head:
        prev_head = head
        head_min_weight = weight
        head_adjoined_nodes = adjoined_nodes
    elif prev_head == head:
        head_min_weight = min(head_min_weight, weight)
        if adjoined_nodes != '{}':
            head_adjoined_nodes = adjoined_nodes
    else:
        print('%s\t%s\t%s' % (prev_head, head_min_weight, head_adjoined_nodes))
        prev_head = head
        head_min_weight = weight
        head_adjoined_nodes = adjoined_nodes

print('%s\t%s\t%s' % (prev_head, head_min_weight, head_adjoined_nodes))
