import time
from typing import List, Tuple

import numpy as np

from calclation import calc_swap_node_cost, calc_total_cost

# type declarations
Coordinate = Tuple[int]
Nodes = List[Coordinate]
Length = float
Path = List[int]


def swap_node(path: Path, i: int, j: int) -> Path:
    tmp = path[i + 1]
    path[i + 1] = path[j]
    path[j] = tmp
    return path


def node_swap(nodes: Nodes, n_node: int, path: Path) -> Tuple[Length, Path]:
    swaped_path = path.copy()
    start = time.time()
    total = 0
    while True:
        count = 0
        for i in range(n_node - 2):
            i_1 = i + 1
            for j in range(i + 2, n_node):
                j_1 = (j + 1) % n_node
                if i != 0 or j_1 != 0:
                    opt2_cost = calc_swap_node_cost(i, i_1, j, j_1, swaped_path, nodes)
                    if opt2_cost < 0:
                        swaped_path = swap_node(swaped_path, i, j)
                        count += 1
        total += count
        if count == 0:
            break
        now = time.time()
        if now - start > 200:
            break

    # path = path.tolist()
    cost = calc_total_cost(nodes, swaped_path)
    return cost, swaped_path


def node_reverse(nodes: Nodes, n_node: int, path: Path) -> Tuple[Length, Path]:
    reversed_path = path.copy()
    start = time.time()
    total = 0
    while True:
        count = 0
        for i in range(n_node - 2):
            i_1 = i + 1
            for j in range(i + 2, n_node):
                j_1 = (j + 1) % n_node

                if i != 0 or j_1 != 0:
                    opt2_cost = calc_swap_node_cost(
                        i, i_1, j, j_1, reversed_path, nodes
                    )
                    if opt2_cost < 0:
                        reversed_path = np.array(reversed_path)
                        new_path = reversed_path[i_1 : j + 1]
                        reversed_path[i_1 : j + 1] = new_path[::-1]
                        count += 1
        total += count
        if count == 0:
            break
        now = time.time()
        if now - start > 200:
            break

    # path = path.tolist()
    cost = calc_total_cost(nodes, reversed_path)
    return cost, reversed_path


def isIntersect(
    node1: Coordinate, node2: Coordinate, node3: Coordinate, node4: Coordinate
) -> bool:
    x1, y1 = node1
    x2, y2 = node2
    x3, y3 = node3
    x4, y4 = node4
    tc1 = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    tc2 = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    td1 = (x3 - x4) * (y1 - y3) + (y3 - y4) * (x3 - x1)
    td2 = (x3 - x4) * (y2 - y3) + (y3 - y4) * (x3 - x2)
    return tc1 * tc2 < 0 and td1 * td2 < 0


def opt_2(path: Path, nodes: Nodes, updated: bool) -> Tuple[Length, Path, bool]:
    n_node = len(path)
    updated = False
    for i in range(n_node - 2):
        a, b = path[i], path[i + 1]
        for j in range(i + 2, n_node):
            c = path[j]
            if j == n_node - 1:
                d = path[0]
            else:
                d = path[j + 1]

            if isIntersect(nodes[a], nodes[b], nodes[c], nodes[d]):
                path[i + 1] = c
                path[j] = b
                path[i + 2 : j] = path[i + 2 : j][::-1]
                updated = True
                break

    cost = calc_total_cost(nodes, path)
    return cost, path, updated
