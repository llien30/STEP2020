from libs import (
    find_shortest_path,
    make_sns_unionfind,
    make_link_list,
    make_change_type_dict,
)
from typing import Dict, List


def check_starwars(
    network,
    start: str,
    goal: str,
    n_characters: int,
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
        print("{} is related to {} :)".format(start, goal))

        check = input(
            "Do you want to check number of paths from {} to {} ? (Y/n) : ".format(
                start, goal
            )
        )
        if check == "n":
            return
        else:
            _, n_path, path = find_shortest_path(
                start_id, goal_id, n_characters, link_list
            )

            name_path = []
            for id in path:
                name = id2name[id]
                name_path.append(name)

            print("Number of shortest paths {} to {} : {}".format(start, goal, n_path))
            example_path = " ⇨ ".join(name_path)
            print("Ex) " + example_path)

    else:
        print("{} is not related to {} :(".format(start, goal))


def main():
    name2id, id2name, n_people = make_change_type_dict("./starwars/names.txt")
    link_list = make_link_list("./starwars/links.txt", n_people)
    network = make_sns_unionfind("./starwars/links.txt", n_people)

    n_groups = network.get_n_groups()
    print("starwars characters are separated into {} groups!".format(n_groups))
    print(network.get_members_dict())
    while True:
        start = input("Enter the name you want to start : ")
        goal = input("Enter the name you want to reach : ")

        check_starwars(network, start, goal, n_people, name2id, id2name, link_list)

        check = input("Do you want to find path more ? (Y/n) : ")
        if check == "n":
            return


if __name__ == "__main__":
    main()
