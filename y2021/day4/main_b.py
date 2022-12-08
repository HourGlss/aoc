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
        self.data = data
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.bingo = False
        self.get_sum_of_all_tiles()

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
        if not self.bingo:
            for y in range(self.height):
                for x in range(self.width):
                    if self.data[y][x].value == called_number:
                        self.data[y][x].tagged = True
                        self.score -= self.data[y][x].value
        self.check_bingo()

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

    def check_bingo(self):
        win = False
        for n in range(5):
            if self.check_col(n) or self.check_row(n):
                win = True
                break
        if win:
            self.bingo = True

    def get_sum_of_all_tiles(self):
        total = 0
        for y in range(self.height):
            for x in range(self.width):
                total += self.data[y][x].value
        self.score = total


class InputHandler:
    draws: list[int]
    boards: list[Board]

    def __init__(self):
        ...

    def handle_draws(self, raw_input):
        self.draws = [int(e) for e in raw_input.split(',')]

    def handle_boards(self, raw_input):
        self.boards = []
        current = 5
        rows = None
        for line in raw_input.split('\n'):
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

    def __init__(self, input_h: InputHandler):
        self.inputHandler = input_h
        self.output = 0
        last_draw, score = self.run_games()
        self.output = last_draw * score

    def run_games(self):
        _ = None
        for draw in self.inputHandler.draws:
            allowed = []
            for board in self.inputHandler.boards:
                board.call(draw)
                if not board.bingo:
                    allowed.append(board)
            _ = draw
            if len(self.inputHandler.boards) == 1 and self.inputHandler.boards[0].bingo:
                break
            self.inputHandler.boards = allowed

        last_board = self.inputHandler.boards[0]
        return _, last_board.score

    def get_output(self):
        return self.output


if __name__ == "__main__":
    from y2021.day4.data import test_draws, test_boards

    inp = InputHandler()
    inp.handle_boards(test_boards)
    inp.handle_draws(test_draws)
    o = OutputHandler(inp)
    print(o.get_output())
