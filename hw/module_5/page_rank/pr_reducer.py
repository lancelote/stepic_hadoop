# coding=utf-8

"""
Реализуйте reducer для алгоритма расчета PageRank с помощью Hadoop Streaming.
Используйте упрощенный алгоритм (без случайных переходов).

Входные и выходные данные: В качестве ключа идет номер вершины. Значение
составное: через табуляцию записано значение PageRank (округленное до 3-го
знака после запятой) и список смежных вершин (через "," в фигурных скобках).

Пример работы reducer приведен для графа из лекции (при этом номера вершин
приведены без n):

Sample Input:

    1	0.067	{}
    1	0.200	{2,4}
    2	0.067	{}
    2	0.100	{}
    2	0.200	{3,5}
    3	0.067	{}
    3	0.100	{}
    3	0.200	{4}
    4	0.100	{}
    4	0.200	{}
    4	0.200	{5}
    5	0.100	{}
    5	0.200	{}
    5	0.200	{1,2,3}

Sample Output:

    1	0.067	{2,4}
    2	0.167	{3,5}
    3	0.167	{4}
    4	0.300	{5}
    5	0.300	{1,2,3}
"""

import sys

prev_node = ''
sum_weight = 0
prev_adjacency = '{}'

for line in sys.stdin:
    node, weight, adjacency_str = line.strip().split('\t')

    if not prev_node:
        if adjacency_str == '{}':
            sum_weight += float(weight)
        else:
            prev_adjacency = adjacency_str

    elif node == prev_node:
        if adjacency_str == '{}':
            sum_weight += float(weight)
        else:
            prev_adjacency = adjacency_str

    else:
        if prev_adjacency == '{}':
            print('%s\t0\t%s' % (prev_node, prev_adjacency))
        else:
            print('%s\t%.3f\t%s' % (prev_node, sum_weight, prev_adjacency))

        if adjacency_str == '{}':
            sum_weight = float(weight)
        else:
            sum_weight = 0
            prev_adjacency = adjacency_str

    prev_node = node

if prev_adjacency == '{}':
    print('%s\t0\t%s' % (prev_node, prev_adjacency))
else:
    print('%s\t%.3f\t%s' % (prev_node, sum_weight, prev_adjacency))
