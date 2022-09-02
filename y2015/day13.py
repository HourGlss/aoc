import itertools
class Node:
    connections: dict[str, int]

    def __init__(self, name):
        self.name = name
        self.connections = dict()
        self.visited = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return_string = f"{self.name}\n"
        for k, v in self.connections.items():
            return_string += f"\t{k} -> {v}\n"
        return return_string


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


def extract_node_weights(input_line: str) -> tuple[str, str, int]:
    pieces = input_line.replace(".", "").split(" ")
    src = pieces[0]
    dst = pieces[len(pieces) - 1]
    weight = int(pieces[3])
    if pieces[2] == "lose":
        weight *= -1

    return src, dst, weight


def split_raw_input_into_lines(raw_input: str) -> list[str]:
    lines = raw_input.split("\n")
    return lines


def build_graph(raw_input: str, g):
    lines = split_raw_input_into_lines(raw_input)
    for line in lines:
        src, dst, weight = extract_node_weights(line)
        g.add_edge(src, dst, weight)

def evaluate_seating_arrangement(input_list:list,g:Graph)->int:

    src = input_list[0]
    dst = input_list[len(input_list)-1]
    total = g.nodes[src].connections[dst] + g.nodes[dst].connections[src]
    # print(0,src,dst,g.nodes[src].connections[dst],g.nodes[dst].connections[src])

    for i,name in enumerate(input_list):
        if i != 0:
            src = name
            dst = input_list[i-1]
            wgt = g.nodes[src].connections[dst]
            wgt2 = g.nodes[dst].connections[src]
            total += wgt+wgt2
    return total


if __name__ == "__main__":
    test_input = """Alice would gain 2 happiness units by sitting next to Bob.
Alice would gain 26 happiness units by sitting next to Carol.
Alice would lose 82 happiness units by sitting next to David.
Alice would lose 75 happiness units by sitting next to Eric.
Alice would gain 42 happiness units by sitting next to Frank.
Alice would gain 38 happiness units by sitting next to George.
Alice would gain 39 happiness units by sitting next to Mallory.
Bob would gain 40 happiness units by sitting next to Alice.
Bob would lose 61 happiness units by sitting next to Carol.
Bob would lose 15 happiness units by sitting next to David.
Bob would gain 63 happiness units by sitting next to Eric.
Bob would gain 41 happiness units by sitting next to Frank.
Bob would gain 30 happiness units by sitting next to George.
Bob would gain 87 happiness units by sitting next to Mallory.
Carol would lose 35 happiness units by sitting next to Alice.
Carol would lose 99 happiness units by sitting next to Bob.
Carol would lose 51 happiness units by sitting next to David.
Carol would gain 95 happiness units by sitting next to Eric.
Carol would gain 90 happiness units by sitting next to Frank.
Carol would lose 16 happiness units by sitting next to George.
Carol would gain 94 happiness units by sitting next to Mallory.
David would gain 36 happiness units by sitting next to Alice.
David would lose 18 happiness units by sitting next to Bob.
David would lose 65 happiness units by sitting next to Carol.
David would lose 18 happiness units by sitting next to Eric.
David would lose 22 happiness units by sitting next to Frank.
David would gain 2 happiness units by sitting next to George.
David would gain 42 happiness units by sitting next to Mallory.
Eric would lose 65 happiness units by sitting next to Alice.
Eric would gain 24 happiness units by sitting next to Bob.
Eric would gain 100 happiness units by sitting next to Carol.
Eric would gain 51 happiness units by sitting next to David.
Eric would gain 21 happiness units by sitting next to Frank.
Eric would gain 55 happiness units by sitting next to George.
Eric would lose 44 happiness units by sitting next to Mallory.
Frank would lose 48 happiness units by sitting next to Alice.
Frank would gain 91 happiness units by sitting next to Bob.
Frank would gain 8 happiness units by sitting next to Carol.
Frank would lose 66 happiness units by sitting next to David.
Frank would gain 97 happiness units by sitting next to Eric.
Frank would lose 9 happiness units by sitting next to George.
Frank would lose 92 happiness units by sitting next to Mallory.
George would lose 44 happiness units by sitting next to Alice.
George would lose 25 happiness units by sitting next to Bob.
George would gain 17 happiness units by sitting next to Carol.
George would gain 92 happiness units by sitting next to David.
George would lose 92 happiness units by sitting next to Eric.
George would gain 18 happiness units by sitting next to Frank.
George would gain 97 happiness units by sitting next to Mallory.
Mallory would gain 92 happiness units by sitting next to Alice.
Mallory would lose 96 happiness units by sitting next to Bob.
Mallory would lose 51 happiness units by sitting next to Carol.
Mallory would lose 81 happiness units by sitting next to David.
Mallory would gain 31 happiness units by sitting next to Eric.
Mallory would lose 73 happiness units by sitting next to Frank.
Mallory would lose 89 happiness units by sitting next to George."""
    g = Graph()
    build_graph(test_input, g)
    # for node_name, node in g.nodes.items():
    #     print(node, end="")
    seating_arrangement = list(g.nodes.keys())
    max_happiness = -1
    for seating in list(itertools.permutations(g.nodes.keys(),len(g.nodes.keys()))):
        current_happiness = evaluate_seating_arrangement(list(seating),g)
        if current_happiness > max_happiness:
            max_happiness = current_happiness
    print(max_happiness)

