# coding=utf-8

"""
Реализуйте алгоритм Дейкстры поиска кратчайшего пути в графе.

Входные данные: В первой строке указаны два числа: число вершин и число ребер
графа. Далее идут строки с описанием ребер. Их количество равно числу ребер.
В каждой строке указаны 3 числа: исходящая вершина, входящая вершина,
вес ребра. В последней строке указаны 2 номера вершины: начальная и конечная
вершина, кратчайший путь между которыми нужно найти.

Выходные данные: минимальное расстояние между заданными вершинами. Если пути
нет, то нужно вернуть -1.

Пример:

    Image: https://ucarecdn.com/56a66a36-361d-4b6b-836f-9a18e751eddd/

Sample Input:

    4 8
    1 2 6
    1 3 2
    1 4 10
    2 4 4
    3 1 5
    3 2 3
    3 4 8
    4 2 1
    1 4

Sample Output:

    9
"""

import sys

node_num, edge_num = None, None
start_node, end_node = None, None
min_weight_array = []

for line in sys.stdin:
    if not node_num:
        node_num, edge_num = line.strip().split()
        min_weight_array = [None]*node_num
        nodes = {i: None for i in range(node_num)}
    elif node_num:
        start, end, weight = line.strip().split()
        if start not in nodes:
            nodes[start] = {end: weight}
        else:
            nodes[start][end] = weight
        node_num -= 1
    else:
        start_node, end_node = line.strip().split()

min_weight_array[start_node] = 0

while min_weight_array[end_node] is not None:
    pass
