from enum import Enum
from y2022.day5.data import test_input, real_input


class Stack:
    crates: list

    def __init__(self):
        self.crates = []

    def add_crate(self, letter):
        self.crates.insert(0, letter)

    def remove_crate(self):
        crate = self.crates.pop(0)
        return crate

    def remove_crates(self,number_of_crates):
        crates = self.crates[0:number_of_crates]
        self.crates = self.crates[number_of_crates:]
        return crates

    def check_top(self):
        if len(self.crates) > 0:
            return self.crates[0]
        return None

    def initial_add_to_bottom(self, letter):
        self.crates.append(letter)

    def move_to(self, number_of_crates: int, stack_to_move_to: "Stack"):
        if number_of_crates == 1:
            crate = self.remove_crate()
            stack_to_move_to.add_crate(crate)
        else:
            crates = self.remove_crates(number_of_crates)
            for c in crates[::-1]:
                stack_to_move_to.add_crate(c)



class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        stacks = None
        letters = [chr(e) for e in range(65, 65 + 26)]
        instructions = []
        for line in input_to_use:

            if stacks is None:
                number_of_stacks = int((len(line) + 1) / 4)
                stacks = [Stack() for e in range(number_of_stacks)]
            if not line.startswith("move"):
                if "1" not in line:
                    stack_number = 1
                    for i in range(0, len(line) + 1, 4):
                        letter = line[i + 1:i + 4 - 2]
                        if letter in letters:
                            stacks[stack_number - 1].initial_add_to_bottom(letter)
                        stack_number += 1
            else:
                if line.startswith("move"):
                    # move 1 from 2 to 1
                    data = line.split(" ")
                    # print(data)
                    from_crate = stacks[int(data[3])-1]
                    to_crate = stacks[int(data[5])-1]
                    amount = int(data[1])
                    instructions.append((from_crate,
                                         to_crate,
                                         amount))

        for i in instructions:
            print("="*10)
            for s in stacks:
                print(s.crates)
            from_crate, to_crate, amount = i
            from_crate.move_to(amount, to_crate)
        print("=" * 10)
        for s in stacks:
            print(s.crates)
        for s in stacks:
            print(s.check_top(),end = "")



class OutputHandler:
    inputHandler: InputHandler

    def __init__(self, i: InputHandler):
        self.inputHandler = i
        self.output = 0
        self.build_output()

    def build_output(self):
        ...

    def get_output(self):
        ...


if __name__ == "__main__":
    i = InputHandler()
    i.handle_raw_input(real_input)
