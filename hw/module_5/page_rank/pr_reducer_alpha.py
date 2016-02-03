# coding=utf-8

"""
Модифицируйте reducer из предыдущего задания так, чтобы он расcчитывал PageRank
с учетом случайного перехода, т.е. первого члена в формуле:

Для всех тестов считайте, что N = 5,  α = 0,1.

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
1	0.080	{2,4}
2	0.170	{3,5}
3	0.170	{4}
4	0.290	{5}
5	0.290	{1,2,3}
"""

import sys

N = 5
ALPHA = 0.1

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
            page_rank = ALPHA/N
        else:
            page_rank = ALPHA/N + (1 - ALPHA)*sum_weight

        print('%s\t%.3f\t%s' % (prev_node, page_rank, prev_adjacency))

        if adjacency_str == '{}':
            sum_weight = float(weight)
        else:
            sum_weight = 0
            prev_adjacency = adjacency_str

    prev_node = node

if prev_adjacency == '{}':
    page_rank = ALPHA/N
else:
    page_rank = ALPHA/N + (1 - ALPHA)*sum_weight

print('%s\t%.3f\t%s' % (prev_node, page_rank, prev_adjacency))
