from libs import (
    find_shortest_path,
    make_train_unionfind,
    make_weighted_link_list,
    make_cheange_type_dict,
)
from typing import Dict, List


def check_train(
    network,
    start: str,
    goal: str,
    n_people: int,
    name2id: Dict,
    id2name: Dict,
    link_list: List,
) -> None:
    if start not in name2id:
        print("Station names {} does not exists :(".format(start))
        return
    if goal not in name2id:
        print("Station names {} does not exists :(".format(goal))
        return

    start_id = name2id[start]
    goal_id = name2id[goal]
    if network.check(start_id, goal_id):
        print("You can go to {} from {} :)".format(goal, start))

        check = input(
            "Do you want to check path from {} to {} ? (Y/n) : ".format(start, goal)
        )
        if check == "n":
            return
        else:
            dist, n_path, path = find_shortest_path(
                start_id, goal_id, n_people, link_list
            )

            name_path = []
            for id in path:
                name = id2name[id]
                name_path.append(name)

            example_path = " ⇨ ".join(name_path)
            print(
                "Path to {} : ".format(goal)
                + example_path
                + "(time : {} min)".format(dist[goal_id])
            )

    else:
        print("You cannot go to {} from {} :(".format(goal, start))


def main():
    name2id, id2name, n_station = make_cheange_type_dict("./train/stations.txt")
    link_list = make_weighted_link_list("./train/edges.txt", n_station)
    network = make_train_unionfind("./train/edges.txt", n_station)

    while True:
        start = input("Enter the station from which you will depart : ")
        goal = input("Enter the station you want to go : ")

        check_train(network, start, goal, n_station, name2id, id2name, link_list)

        check = input("Do you want to find path more ? (Y/n) : ")
        if check == "n":
            return


if __name__ == "__main__":
    main()
