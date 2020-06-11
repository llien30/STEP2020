import heapq
from typing import Dict, List, Tuple

Name2Id = Dict[str, int]
Id2Name = Dict[int, str]


def dijkstra(
    start: int, n_nodes: int, edge: List[List[int]]
) -> Tuple[List[int], List[int], List[int]]:

    dist = [float("inf")] * n_nodes
    dist[start] = 0
    n_ways = [0] * n_nodes
    prev = [-1] * n_nodes
    n_ways[start] = 1
    # make heapq
    q = [(dist[start], start)]

    heapq.heapify(q)
    while q:
        # pop the nearest node from start
        d, i = heapq.heappop(q)

        # continue when the distance is larger than the recorded distance
        if dist[i] < d:
            continue
        # find the node go next
        for cost, j in edge[i]:
            if dist[j] > dist[i] + cost:
                dist[j] = dist[i] + cost
                n_ways[j] = n_ways[i]
                prev[j] = i
                heapq.heappush(q, (dist[j], j))

            elif dist[j] == dist[i] + cost:
                n_ways[j] += n_ways[i]
    return dist, n_ways, prev


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parent = [i for i in range(n_nodes)]
        self.rank = [1] * n_nodes
        self.size = [1] * n_nodes

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):

        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

    def get_parent_list(self):
        return [i for i in range(self.n_nodes) if self.find(i) == i]

    def get_n_groups(self):
        return len(self.get_parent_list())

    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def make_cheange_type_dict(filename: str) -> Tuple[Name2Id, Id2Name, int]:
    """make Name2Id and Id2Name dictionary

    Name2Id : input name -> output id
    Id2Name : input id -> output name
    n_nodes : number of nodes

    """

    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split("\n")

    name2id = {}
    id2name = {}

    for line in lines:
        line = list(line.split())

        if not line:
            continue

        id = int(line[0])
        name = line[1]
        name2id[name] = id
        id2name[id] = name
        n_nodes = id + 1

    return name2id, id2name, n_nodes


def make_link_list(filename: str, n_nodes: int) -> List[List[int]]:
    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split("\n")

    link_list = [[] for _ in range(n_nodes)]

    for line in lines:
        if not line:
            continue

        id_1, id_2 = map(int, line.split())
        link_list[id_1].append((1, id_2))
        link_list[id_2].append((1, id_1))

    return link_list


def make_weighted_link_list(filename: str, n_nodes: int) -> List[List[int]]:
    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split("\n")

    link_list = [[] for _ in range(n_nodes)]

    for line in lines:
        if not line:
            continue

        id_1, id_2, time = map(int, line.split())
        link_list[id_1].append((time, id_2))
        link_list[id_2].append((time, id_1))

    return link_list


def make_sns_unionfind(filename: str, n_nodes: int):
    UF = UnionFind(n_nodes)

    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split("\n")

    for line in lines:
        if not line:
            continue

        id_1, id_2 = map(int, line.split())
        UF.unite(id_1, id_2)

    return UF


def make_train_unionfind(filename: str, n_nodes: int):
    UF = UnionFind(n_nodes)

    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split("\n")

    for line in lines:
        if not line:
            continue
        id_1, id_2, _ = map(int, line.split())
        UF.unite(id_1, id_2)

    return UF


def make_wikipedia_unionfind(filename: str, n_nodes: int):
    UF = UnionFind(n_nodes)

    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split("\n")

    for line in lines:
        if not line:
            continue
        id_1, id_2 = map(int, line.split())
        UF.unite(id_1, id_2)

    return UF


def find_shortest_path(
    start: int, goal: int, n_node: int, edge: List[List[int]]
) -> Tuple[int, List[int]]:

    dist, n_ways, prev = dijkstra(start, n_node, edge)
    n_paths = n_ways[goal]
    path = [goal]
    node = goal

    while node != start:
        node = prev[node]
        path.append(node)

    path = path[::-1]

    return dist, n_paths, path
