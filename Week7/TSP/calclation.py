import math
from typing import List, Tuple

# type declarations
Coordinate = Tuple[int]
Nodes = List[Coordinate]
Length = float


def distance(node1: Coordinate, node2: Coordinate) -> float:
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_angle(node1: Coordinate, node2: Coordinate) -> float:
    """Calculate angle viewed from node1
    """
    x1, y1 = node1
    x2, y2 = node2
    theta = math.atan2(y2 - y1, x2 - x1)
    if theta < 0:
        theta = (2 * math.pi) + theta
    return theta


def calc_insert_cost(node1: Coordinate, node2: Coordinate, node3: Coordinate) -> float:
    """
    Calculate (node1 -> node3) + (node3 -> node2) - (node1 -> node2)
    """
    dist13 = distance(node1, node3)
    dist32 = distance(node2, node3)
    dist12 = distance(node1, node2)
    return dist13 + dist32 - dist12


def calc_total_cost(nodes: Nodes, path: List[int]) -> float:
    total_cost = 0
    for i in range(len(nodes)):
        total_cost += distance(nodes[path[i]], nodes[path[i - 1]])
    return total_cost


def calc_cost_ratio(node1: Coordinate, node2: Coordinate, node3: Coordinate) -> float:
    """
    Calculate {(node1 -> node3) + (node3 -> node2)} / (node1 -> node2)
    """
    dist13 = distance(node1, node3)
    dist32 = distance(node2, node3)
    dist12 = distance(node1, node2)
    return (dist13 + dist32) / dist12


def calc_swap_node_cost(i, i_1, j, j_1, path, nodes):
    l1 = distance(nodes[path[i]], nodes[path[i_1]])
    l2 = distance(nodes[path[j]], nodes[path[j_1]])
    l3 = distance(nodes[path[i]], nodes[path[j]])
    l4 = distance(nodes[path[i_1]], nodes[path[j_1]])
    return l3 + l4 - (l1 + l2)
