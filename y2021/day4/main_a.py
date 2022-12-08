class Tile:
    value: int
    tagged: bool

    def __init__(self, val: int):
        self.value = val
        self.tagged = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        ret = f"{self.value}"
        if self.tagged:
            ret += "!"
        return ret


class Board:
    data: list[list[Tile]]
    bingo: bool
    score: int

    def __init__(self, data: list[list[Tile]]):
        self.score = -1
        self.data = data
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.bingo = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        ret = ""
        for y in range(self.height):
            for x in range(self.width):
                ret += f"{str(self.data[y][x]):>3} "
            ret += '\n'
        return ret

    def call(self, called_number: int):
        for y in range(self.height):
            for x in range(self.width):
                if self.data[y][x].value == called_number:
                    self.data[y][x].tagged = True

    def check_row(self, row_to_check):
        for y in range(self.height):
            if not self.data[y][row_to_check].tagged:
                return False
        return True

    def check_col(self, col_to_check):
        for x in range(self.width):
            if not self.data[col_to_check][x].tagged:
                return False
        return True

    def check_bingo_and_score(self):
        win = False
        for i in range(5):
            if self.check_col(i) or self.check_row(i):
                win = True
                break
        if win:
            self.bingo = True
            self.score = self.get_sum_of_all_unmarked_numbers()

    def get_sum_of_all_unmarked_numbers(self):
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                if not self.data[y][x].tagged:
                    total += self.data[y][x].value
        return total


class InputHandler:
    draws: list[int]
    boards: list[Board]

    def __init__(self):
        ...

    def handle_draws(self, raw_input):
        draws = raw_input.split(',')
        self.draws = [int(e) for e in draws]

    def handle_boards(self, raw_input):
        lines = raw_input.split('\n')
        self.boards = []
        current = 5
        rows = None
        for line in lines:
            line = line.strip()
            line = line.replace("  ", " ")
            if current == 5:
                rows = []
            if line != "":
                row = [Tile(int(_)) for _ in line.split(" ")]
                rows.append(row)
                current -= 1
                if current == 0:
                    self.boards.append(Board(rows))
                    current = 5


class OutputHandler:
    inputHandler: InputHandler
    output: int

    def __init__(self, i: InputHandler):
        self.inputHandler = i
        self.output = 0
        last_draw, score = self.run_games()
        self.output = last_draw * score

    def run_games(self):
        done = False
        for draw in self.inputHandler.draws:
            for board in self.inputHandler.boards:
                board.call(draw)
                board.check_bingo_and_score()
                if board.bingo:
                    self.output = board.score
                    return draw, board.score

    def get_output(self):
        return self.output


if __name__ == "__main__":
    from y2021.day4.data import test_draws, test_boards

    i = InputHandler()
    i.handle_boards(test_boards)
    i.handle_draws(test_draws)
    o = OutputHandler(i)
    print(o.get_output())