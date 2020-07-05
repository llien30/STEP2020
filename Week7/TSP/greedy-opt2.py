import argparse

from edit_file import plot_path, read_csv, save_path
from libs import greedy_search
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


def main():
    args = get_arguments()
    n_cities, cities = read_csv(f"input_{args.file_number}.csv")

    min_path = ""
    min_cost = float("inf")
    # for start_node in range(n_cities):

    # start_node = 8  # for challenge 2
    start_node = 112  # for challenge6
    # start_node = 0
    cost, path = greedy_search(n_cities, cities, start_node)
    print(f"Greedy cost({start_node}): {cost}")

    reverse_cost, reverse_path = node_reverse(cities, n_cities, path)

    if cost < reverse_cost:
        min_cost = cost
        min_path = path
    else:
        min_cost = reverse_cost
        min_path = reverse_path

    print(f"Reversed cost({start_node}):{reverse_cost}")

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

    plot_path(path, cities, f"./image/greedy_{args.file_number}.png")
    plot_path(min_path, cities, f"./image/greedy_2-opt{args.file_number}.png")
    print(f"min length (iteration : {iteration}): {min_cost}")
    save_path(f"output_{args.file_number}.csv", min_path)


if __name__ == "__main__":
    main()
