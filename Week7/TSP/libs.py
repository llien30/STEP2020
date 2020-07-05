from itertools import permutations
from typing import List, Tuple

import numpy as np

from calclation import (
    calc_cost_ratio,
    calc_insert_cost,
    calc_total_cost,
    distance,
    get_angle,
)

# type declarations
Coordinate = Tuple[int]
Nodes = List[Coordinate]
Length = float
Path = List[int]


def search_all_path(n_node: int, nodes: Nodes) -> Tuple[float, List]:
    permutation = list(permutations(range(n_node)))
    shortest_path_length = float("inf")
    shortest_parh = []

    for path in permutation:
        path = list(path)
        path_length = calc_total_cost(nodes, path)

        if shortest_path_length > path_length:
            shortest_path_length = path_length
            shortest_parh = path

    return shortest_path_length, shortest_parh


def greedy_search(n_node: int, nodes: Nodes, start_node: int) -> Tuple[Length, Path]:
    dist = [[0] * n_node for i in range(n_node)]
    for i in range(n_node):
        for j in range(i, n_node):
            dist[i][j] = dist[j][i] = distance(nodes[i], nodes[j])

    current_node = start_node
    unvisited_node = set(range(n_node))
    unvisited_node.remove(start_node)
    path = [current_node]
    path_length = 0

    while unvisited_node:
        next_node = min(unvisited_node, key=lambda node: dist[current_node][node])
        unvisited_node.remove(next_node)

        path.append(next_node)
        path_length += dist[current_node][next_node]

        current_node = next_node

    return path_length, path


def graham_scan(n_node: int, node: Nodes) -> Tuple[Length, Path]:
    min = 0
    # Find the node with the smallest y-coordinate
    for i in range(n_node):
        if node[min][1] > node[i][1]:
            min = i
        elif node[min][1] == node[i][1] and node[min][0] > node[i][0]:
            min = i

    angle = np.zeros((n_node, 2))
    for i in range(n_node):
        if i == min:
            angle[i] = [0, i]
        else:
            theta = get_angle(node[i], node[min])
            angle[i] = [theta, i]

    sorted_angle = angle[angle[:, 0].argsort(), :]
    # print(sorted_angle)

    path = []
    path.extend(
        [int(sorted_angle[0, 1]), int(sorted_angle[1, 1]), int(sorted_angle[2, 1])]
    )

    for i in range(3, n_node):
        path_top = len(path)
        while True:
            theta1 = get_angle(node[path[path_top - 2]], node[path[path_top - 1]])
            theta2 = get_angle(node[path[path_top - 1]], node[int(sorted_angle[i, 1])])

            if theta2 - theta1 < 0:
                del path[path_top - 1]
                path_top -= 1
            else:
                break
        path.append(int(sorted_angle[i, 1]))
        # print(path)
    return path


def insert(path: Path, nodes: Nodes) -> Tuple[Length, Path]:
    ex_path = [i for i in range(len(nodes))]
    for node in path:
        ex_path.remove(node)

    while True:
        min = 0
        costratio = [0 for i in range(len(path))]
        min_node = [0 for i in range(len(path))]
        for i in range(len(path)):
            for j in range(0, len(ex_path)):
                cost = calc_insert_cost(
                    nodes[path[i - 1]], nodes[path[i]], nodes[ex_path[j]]
                )
                if j == 0 or min > cost:
                    min = cost
                    min_node[i] = ex_path[j]
            costratio[i] = calc_cost_ratio(
                nodes[path[i - 1]], nodes[path[i]], nodes[min_node[i]]
            )

        min_ratio = 10 ** 9
        min_ratio_place = 0

        for i in range(len(path)):
            if min_ratio > costratio[i]:
                min_ratio = costratio[i]
                min_ratio_place = i

        path.insert(min_ratio_place, min_node[min_ratio_place])
        ex_path.remove(min_node[min_ratio_place])

        if not ex_path:
            break

    cost = calc_total_cost(nodes, path)
    return cost, path
