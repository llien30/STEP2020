from typing import List, Tuple

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

# type declarations
Coordinate = Tuple[int]
Nodes = List[Coordinate]
Path = List[int]


def read_csv(filename: str) -> Tuple[int, Nodes]:
    with open(filename, "r") as f:
        node = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(",")
            node.append((float(xy[0]), float(xy[1])))
        n_node = len(node)
        return n_node, node


def save_path(filename: str, path: Path) -> None:
    with open(filename, "w") as f:
        f.write("index\n")
        for node in path:
            f.write(f"{node}\n")


def plot_path(path: Path, nodes: Nodes, save_fig_path: str) -> None:
    plt.clf()
    X = []
    Y = []
    for x, y in nodes:
        X.append(x)
        Y.append(y)
    plt.scatter(X, Y)
    for i, number in enumerate(path):
        x, y = nodes[number]
        plt.scatter(x, y, c="red")
        if i == 0:
            beforenode = number
            initnode = number
        else:
            x1, y1 = nodes[beforenode]
            x2, y2 = nodes[number]
            plt.plot([x1, x2], [y1, y2], "r")
            beforenode = number

    x1, y1 = nodes[beforenode]
    x2, y2 = nodes[initnode]
    plt.plot([x1, x2], [y1, y2], "r")

    plt.savefig(save_fig_path)
