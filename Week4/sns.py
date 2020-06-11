from libs import (
    find_shortest_path,
    make_sns_unionfind,
    make_link_list,
    make_cheange_type_dict,
)
from typing import Dict, List


def check_sns(
    network,
    start: str,
    goal: str,
    n_people: int,
    name2id: Dict,
    id2name: Dict,
    link_list: List,
) -> None:
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
            _, n_path, path = find_shortest_path(start_id, goal_id, n_people, link_list)

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
    name2id, id2name, n_people = make_cheange_type_dict("./sns/nicknames.txt")
    link_list = make_link_list("./sns/links.txt", n_people)
    network = make_sns_unionfind("./sns/links.txt", n_people)

    print("Number of groups of this SNS: %d" % network.get_n_groups())

    goal = input("Enter who you want to find path from 'adrian' : ")

    check_sns(network, "adrian", goal, n_people, name2id, id2name, link_list)

    while True:
        check = input("Do you want to find path more ? (Y/n) : ")
        if check == "n":
            return

        start = input("Enter the nickname you want to start : ")
        goal = input("Enter the nickname you want to reach : ")

        check_sns(network, start, goal, n_people, name2id, id2name, link_list)


if __name__ == "__main__":
    main()
