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
from collections import defaultdict


def read_data():
    """Читаем данные"""
    graph = defaultdict(dict)
    start = None
    end = None
    edge_num = None
    node_num = None

    for line in sys.stdin:
        if edge_num is None:
            node_num, edge_num = map(int, line.strip().split())
        elif edge_num:
            from_node, to_node, weight = line.strip().split()
            graph[from_node][to_node] = weight
            edge_num -= 1
        else:
            start, end = line.strip().split()
    return start, end, node_num, graph


def dijkstra():
    """Ищем расстояние между двумя вершинами"""
    start, end, node_num, graph = read_data()  # Загружаем данные

    distances = [9999]*int(node_num)  # Список расстояний до вершин
    distances[int(start) - 1] = 0     # Расстояние до стартовой вершины - 0

    unknown_nodes = graph.copy()      # Вершины с неизвестным расстоянием

    while unknown_nodes:
        # Выбираем ближайшую вершину из непосещенных
        nearest_node = min(unknown_nodes, key=lambda x: distances[int(x) - 1])

        # Перебираем соединенные с ближайшей вершины
        for node, weight in unknown_nodes[nearest_node].items():

            # Если нашли путь короче - обновляем список расстояний
            if distances[int(node) - 1] > distances[int(nearest_node) - 1] +\
                    int(weight):
                distances[int(node) - 1] = distances[int(nearest_node) - 1] +\
                                           int(weight)

        del unknown_nodes[nearest_node]  # Удаляем посещенную вершину

    answer = distances[int(end) - 1]  # Расстояние до требуемой вершины
    return answer if answer != 9999 else -1

print(dijkstra())
