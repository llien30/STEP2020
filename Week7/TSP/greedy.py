import argparse

from edit_file import plot_path, read_csv, save_path
from libs import greedy_search
from optimization import node_reverse, node_swap, opt_2


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
    for start_node in range(n_cities):
        cost, path = greedy_search(n_cities, cities, start_node)
        print(f"Greedy cost({start_node}): {cost}")

        cost_opt, opt_2_path = opt_2(path, cities)
        print(f"After 2-opt({start_node}) :{cost_opt}")
        if cost < min_cost:
            min_cost = cost
            min_path = path

        if cost_opt < min_cost:
            min_cost = cost_opt
            min_path = opt_2_path

        cost1, swap_path = node_swap(cities, n_cities, path)
        print(f"After 2-opt swap: {cost1}")
        plot_path(swap_path, cities, f"./image/greedy_2opt-swap_{args.file_number}.png")

        if cost1 < min_cost:
            min_cost = cost1
            min_path = swap_path

        cost2, reverse_path = node_reverse(cities, n_cities, path)
        print(f"After 2-opt reverse: {cost2}")
        plot_path(
            reverse_path, cities, f"./image/greedy_2opt-reverse_{args.file_number}.png"
        )

        if cost2 < min_cost:
            min_cost = cost2
            min_path = reverse_path

    plot_path(min_path, cities, f"./image/greedy_{args.file_number}.png")
    print(f"min length : {min_cost}")
    save_path(f"output_{args.file_number}.csv", min_path)


if __name__ == "__main__":
    main()
