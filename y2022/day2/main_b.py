from enum import Enum
from y2022.day2.data import test_input, real_input

"""
1 for Rock, 2 for Paper, and 3 for Scissors
(0 if you lost, 3 if the round was a draw, and 6 if you won)


"""
class InputHandler:
    elements: list


    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        total = 0
        for line in input_to_use:
            datas = line.split(" ")
            theirs = datas[0]
            outcome = datas[1]
            score = 0

            if outcome == "X":
                #lose
                if theirs == "A":
                    # ROCK
                    score += 3
                elif theirs == "B":
                    # PAPER
                    score += 1
                elif theirs == "C":
                    # SCIZZ
                    score += 2
            elif outcome == "Y":
                # tie
                score += 3
                if theirs == "A":
                    # ROCK
                    score += 1
                elif theirs == "B":
                    # PAPER
                    score += 2
                elif theirs == "C":
                    # SCIZZ
                    score += 3
            elif outcome == "Z":
                # win
                score += 6
                if theirs == "A":
                    # ROCK
                    score += 2
                elif theirs == "B":
                    # PAPER
                    score += 3
                elif theirs == "C":
                    # SCIZZ\
                    score += 1

            total += score

        self.total = total


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
    print(i.total)
