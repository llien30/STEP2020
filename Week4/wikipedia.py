from libs import (
    find_shortest_path,
    make_change_type_dict,
    make_one_way_link,
    make_wikipedia_unionfind,
)


def check_wikipedia(network, start, goal, n_pages, name2id, id2name, link_list):
    if start not in name2id:
        print("{} does not exists :(".format(start))
        return
    if goal not in name2id:
        print("{} does not exists :(".format(goal))
        return

    start_id = name2id[start]
    goal_id = name2id[goal]
    if network.check(start_id, goal_id):
        print("{} can reach to {} :)".format(start, goal))

        check = input(
            "Do you want to check number of paths from {} to {} ? (Y/n) : ".format(
                start, goal
            )
        )
        if check == "n":
            return
        else:
            _, n_path, path = find_shortest_path(start_id, goal_id, n_pages, link_list)
            name_path = []
            for id in path:
                name = id2name[id]
                name_path.append(name)

            print("Number of shortest paths {} to {} : {}".format(start, goal, n_path))
            example_path = " ⇨ ".join(name_path)
            print("Ex) " + example_path)

    else:
        print("{} cannot reach to {} :(".format(start, goal))


def main():
    name2id, id2name, n_pages = make_change_type_dict("./wikipedia/pages.txt")
    # id2name = make_id2name("./wikipedia/pages.txt")

    wikipedia_network = make_wikipedia_unionfind("./wikipedia/links.txt", n_pages)

    link = make_one_way_link("./wikipedia/links.txt", n_pages)

    n_groups = wikipedia_network.get_n_groups()
    print("Wikipedia is separated into {}-th groups!!".format(n_groups))

    while True:
        start = input("Enter the name you want to start : ")
        goal = input("Enter the name you want to reach : ")

        check_wikipedia(wikipedia_network, start, goal, n_pages, name2id, id2name, link)

        check = input("Do you want to find path more ? (Y/n) : ")
        if check == "n":
            return


if __name__ == "__main__":
    main()
