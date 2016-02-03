# coding=utf-8

"""
Реализуйте mapper для алгоритма расчета PageRank с помощью Hadoop Streaming.

Входные и выходные данные: В качестве ключа идет номер вершины. Значение
составное: через табуляцию записано значение PageRank (округленное до 3-го
знака после запятой) и список смежных вершин (через "," в фигурных скобках).

Пример работы mapper приведен для графа из лекции (при этом номера вершин
приведены без n):

Sample Input:

    1	0.200	{2,4}
    2	0.200	{3,5}
    3	0.200	{4}
    4	0.200	{5}
    5	0.200	{1,2,3}

Sample Output:

    1	0.200	{2,4}
    2	0.100	{}
    4	0.100	{}
    2	0.200	{3,5}
    3	0.100	{}
    5	0.100	{}
    3	0.200	{4}
    4	0.200	{}
    4	0.200	{5}
    5	0.200	{}
    5	0.200	{1,2,3}
    1	0.067	{}
    2	0.067	{}
    3	0.067	{}
"""

import sys


def convert_to_list(str_format):
    if str_format == '{}':
        return []
    else:
        return str_format[1:-1].split(',')

for line in sys.stdin:
    head, page_rank, adjacency_str = line.strip().split('\t')
    adjacency_list = convert_to_list(adjacency_str)

    try:
        probability = float(page_rank)/len(adjacency_list)
    except ZeroDivisionError:
        continue

    print(line.strip())

    for node in adjacency_list:
        print('%s\t%.3f\t{}' % (node, probability))
