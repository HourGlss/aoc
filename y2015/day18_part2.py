class Grid:
    lights: list[list[int]]

    def __init__(self, input_string: str):
        lights = []
        for line in input_string.split("\n"):
            current_row = []
            for c in line.strip():
                if c == ".":
                    current_row.append(0)
                else:
                    current_row.append(1)
            lights.append(current_row)
        self.lights = lights

    def keep_broken_lights_on(self):
        self.lights[0][0] = 1
        self.lights[len(self.lights)-1][0] = 1
        self.lights[0][len(self.lights)-1] = 1
        self.lights[len(self.lights)-1][len(self.lights)-1] = 1

    def print_lights(self):
        for y in range(len(self.lights)):
            for x in range(len(self.lights[0])):
                if self.lights[y][x] == 1:
                    c = "#"
                else:
                    c = "."
                print(c, end="")
            print()

    def get_neighbors(self, y, x):
        neighbors = []
        # north
        if y - 1 >= 0:
            neighbors.append(self.lights[y - 1][x])
        # south
        if y + 1 < len(self.lights):
            neighbors.append(self.lights[y + 1][x])
        # east
        if x + 1 < len(self.lights[0]):
            neighbors.append(self.lights[y][x + 1])
        # west
        if x - 1 >= 0:
            neighbors.append(self.lights[y][x - 1])
        # se
        if x + 1 < len(self.lights[0]) and y + 1 < len(self.lights):
            neighbors.append(self.lights[y + 1][x + 1])
        # sw
        if y + 1 < len(self.lights) and x - 1 >= 0:
            neighbors.append(self.lights[y + 1][x - 1])
        # ne
        if y - 1 >= 0 and x + 1 < len(self.lights[0]):
            neighbors.append(self.lights[y - 1][x + 1])
        # nw
        if x - 1 >= 0 and y - 1 >= 0:
            neighbors.append(self.lights[y - 1][x - 1])
        return neighbors

    def transition(self):
        # print("+"*10)
        new_lights = []
        for y in range(len(self.lights)):
            new_row = []
            for x in range(len(self.lights[0])):
                number_of_lit_neighbors = sum(self.get_neighbors(y, x))
                if self.lights[y][x] == 1:
                    if number_of_lit_neighbors == 2 or number_of_lit_neighbors == 3:
                        new_row.append(1)
                    else:
                        new_row.append(0)
                elif self.lights[y][x] == 0:
                    if number_of_lit_neighbors == 3:
                        new_row.append(1)
                    else:
                        new_row.append(0)
            new_lights.append(new_row)
        self.lights = new_lights

    def count_lit_lights(self):
        total = 0
        for y in range(len(self.lights)):
            for x in range(len(self.lights[0])):
                total += self.lights[y][x]
        return total

if __name__ == "__main__":
    example_state = """.#.#.#
    ...##.
    #....#
    ..#...
    #.#..#
    ####.."""
    from day18_data import data
    g = Grid(data)
    g.keep_broken_lights_on()
    # g.print_lights()
    for i in range(100):
        g.transition()
        g.keep_broken_lights_on()
        # g.print_lights()
    print(g.count_lit_lights())

