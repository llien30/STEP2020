import argparse

from christofides_parts import (
    build_graph,
    find_eulerian_tour,
    find_odd_vertexes,
    minimum_spanning_tree,
    minimum_weight_matching,
)
from edit_file import plot_path, read_csv, save_path
from optimization import node_reverse, opt_2


def get_arguments():
    """
    make parser to get parameters
    """

    parser = argparse.ArgumentParser(description="get number of csv file")

    parser.add_argument(
        "file_number", type=int, help="number of file to search shortest path"
    )

    return parser.parse_args()


def christofides(nodes):
    G = build_graph(nodes)

    MSTree = minimum_spanning_tree(G)
    odd_vertexes = find_odd_vertexes(MSTree)

    minimum_weight_matching(MSTree, G, odd_vertexes)

    eulerian_tour = find_eulerian_tour(MSTree, G)

    current = eulerian_tour[0]
    path = [current]

    visited = [False] * len(eulerian_tour)
    visited[current] = True

    length = 0

    for v in eulerian_tour[1:]:
        if not visited[v]:
            visited[v] = True
            length += G[current][v]
            path.append(v)
            current = v

    return length, path


def main():
    args = get_arguments()
    n_cities, cities = read_csv(f"input_{args.file_number}.csv")

    length, path = christofides(cities)
    # print(path)
    print(f"cost : {length}")
    plot_path(path, cities, f"./image/christofides_{args.file_number}.png")

    min_cost = length
    min_path = path

    iteration = 0
    updated = True
    while updated:
        cost_opt, opt_2_path, updated = opt_2(min_path, cities, updated)

        if cost_opt < min_cost:
            min_path = opt_2_path
            min_cost = cost_opt

        if iteration % 10 == 0:
            print(f"After {iteration} iteration : {min_cost}")

        iteration += 1

    print(f"final cost : {min_cost}")
    plot_path(min_path, cities, f"./image/christofides_2opt_{args.file_number}.png")

    # save_path(f"output_{args.file_number}.csv", min_path)


if __name__ == "__main__":
    main()
