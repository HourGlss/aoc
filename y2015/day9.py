import copy


class Node:
    connections: dict[str, int]

    def __init__(self, name):
        self.name = name
        self.connections = dict()
        self.visited = False


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    nodes: dict[str, Node]

    def __init__(self):
        self.nodes = dict()

    # Function to add an edge in an undirected graph
    def add_edge(self, src: str, dest: str, weight: int):
        # Adding the node to the source node
        if src not in self.nodes.keys():
            snode = Node(src)
            self.nodes[src] = snode
        if dest not in self.nodes.keys():
            dnode = Node(dest)
            self.nodes[dest] = dnode
        self.nodes[src].connections[dest] = weight
        self.nodes[dest].connections[src] = weight


def build_short_path(n: Node, _g, path: list) -> list[str]:
    n.visited = True
    path.append(n.name)
    # print(f"at {n.name} path is currently {path}")
    shortest = -1
    next_node = None
    for k, v in n.connections.items():
        next = _g.nodes[k]
        if not next.visited:
            if shortest == -1:
                shortest = v
                next_node = next
            else:
                if v < shortest:
                    shortest = v
                    next_node = next
    if next_node is None:
        return path
    else:
        return build_short_path(next_node, _g, path)


def build_long_path(n: Node, _g, path: list) -> list[str]:
    n.visited = True
    path.append(n.name)
    # print(f"at {n.name} path is currently {path}")
    best = -1
    next_node = None
    for name_of_city, distance in n.connections.items():
        current_eval = _g.nodes[name_of_city]
        if not current_eval.visited:
            if best == -1:
                best = distance
                next_node = current_eval
            else:
                if distance > best:
                    best = distance
                    next_node = current_eval
    if next_node is None:
        return path
    else:
        return build_long_path(next_node, _g, path)


def get_length_of_path(_p: list[str], _g) -> int:
    total = 0
    for i, n in enumerate(_p):
        if i != 0:
            dst = _g.nodes[_p[i]]
            src = _g.nodes[_p[i - 1]]
            total += src.connections[dst.name]
    return total


longest = 0


def build_every_path(_n: str, _g: Graph, _path: list):
    global longest
    if len(_path) == 8:
        current = get_length_of_path(_path, _g)
        print(_path)
        if current > longest:
            longest = current
            print(longest)
        return
    _path.append(_n)
    for city in _path:
        _g.nodes[city].visited = True
    next_node = None
    for k, v in _g.nodes[_n].connections.items():
        if not _g.nodes[k].visited:
            next_node = _g.nodes[k]
            # print(f"\tnext {next_node.name}")
            curr_g = create_graph(raw_input)[0]
            for city in _path:
                curr_g.nodes[city].visited = True
            build_every_path(k, curr_g, _path)


def part2(_input):
    _g, _cities = _input
    copy_of_graph, x = create_graph(raw_input)
    for city in _cities:
        node = _g.nodes[city]
        path = []
        # _ = build_long_path(node, _g, path)
        # print(get_length_of_path(_, _g), path)
        _ = build_short_path(node, _g, path)
        print(get_length_of_path(_, _g), path)


def part1(_input) -> int:
    _g, _cities = _input
    shortest = -1
    for city in _cities:
        path = []
        path = build_short_path(_g.nodes[city], _g, path)
        # print(path)
        length = get_length_of_path(path, _g)
        for n in _g.nodes.values():
            n.visited = False
        if shortest == -1:
            shortest = length
        else:
            if length < shortest:
                shortest = length
    return shortest


def create_graph(_s: str) -> tuple[Graph, list[str]]:
    cities = dict()
    test_list = _s.split("\n")
    for line in test_list:
        pieces = line.split(" ")
        if pieces[0] not in cities.keys():
            cities[pieces[0]] = len(cities.keys())
        if pieces[2] not in cities.keys():
            cities[pieces[2]] = len(cities.keys())
    graph = Graph()
    for line in test_list:
        pieces = line.split(" ")
        graph.add_edge(pieces[0], pieces[2], int(pieces[4]))
    return graph, list(cities.keys())


def part2_perms(_input):
    _g, _cities = _input
    from itertools import permutations
    all = list(permutations(_cities, len(_cities)))
    longest = 0
    shortest = -1
    for path in all:
        try:
            i = get_length_of_path(path, _g)
            if i > longest:
                longest = i
                print(longest, path)
            if shortest == -1 or i < shortest:
                shortest = i
                # print(shortest, path)
        except:
            pass


if __name__ == "__main__":
    raw_input = """Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70"""
    print(part1(create_graph(raw_input)))
