class Aunt:
    children: int | None
    cats: int | None
    samoyeds: int | None
    pomeranians: int | None
    akitas: int | None
    vizslas: int | None
    goldfish: int | None
    trees: int | None
    cars: int | None
    perfumes: int | None
    aunt_number: int

    def __init__(self, attributes_dict, i):
        self.aunt_number = i
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None
        for k, v in attributes_dict.items():
            self.__setattr__(k, v)

    def test(self, other):
        attributes = ["children",
                      "cats",
                      "samoyeds",
                      "pomeranians",
                      "akitas",
                      "vizslas",
                      "goldfish",
                      "trees",
                      "cars",
                      "perfumes"]
        possible = True
        for attribute in attributes:
            if other.__getattribute__(attribute) is not None:
                if other.__getattribute__(attribute) != self.__getattribute__(attribute):
                    possible = False
                    break
        return possible

    def test2(self, other):
        attributes = ["children",
                      "cats",
                      "samoyeds",
                      "pomeranians",
                      "akitas",
                      "vizslas",
                      "goldfish",
                      "trees",
                      "cars",
                      "perfumes"]
        part2 = ['cats', 'trees', 'pomeranians', "goldfish"]
        possible = True
        for attribute in attributes:
            if attribute not in part2:
                if other.__getattribute__(attribute) is not None:
                    if other.__getattribute__(attribute) != self.__getattribute__(attribute):
                        possible = False
                        break
            else:
                if other.__getattribute__(attribute) is not None:
                    if attribute == "cats" or attribute == "trees":
                        if self.__getattribute__(attribute) > other.__getattribute__(attribute):
                            possible = False
                            break
                    if attribute == "pomeranians" or attribute == "goldfish":
                        if self.__getattribute__(attribute) < other.__getattribute__(attribute):
                            possible = False
                            break
        return possible


def build_other_aunts(input_string: str):
    aunts = []
    for line in input_string.split('\n'):
        pieces = line.split(" ")
        # print(pieces)
        data = {}
        data[pieces[2][:len(pieces[2]) - 1]] = int(pieces[3][:len(pieces[3]) - 1])
        data[pieces[4][:len(pieces[4]) - 1]] = int(pieces[5][:len(pieces[5]) - 1])
        data[pieces[6][:len(pieces[6]) - 1]] = int(pieces[7])
        aunts.append(Aunt(data, int(pieces[1][:len(pieces[1]) - 1])))
        # print(data)
        # break
    return aunts


if __name__ == "__main__":
    correct = Aunt({
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }, 0)
    from day16_input import raw_input

    aunts = build_other_aunts(raw_input)
    for aunt in aunts:
        if correct.test2(aunt):
            print(aunt.aunt_number)
