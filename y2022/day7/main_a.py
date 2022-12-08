from enum import Enum
from y2022.day7.data import test_input, real_input


class Commands:

    @staticmethod
    def change_directory(pwd: str, path_to_change_to: str):
        if path_to_change_to == "..":
            pwd = pwd[0:len(pwd) - 1]
            slashes = []
            for i, c in enumerate(pwd):
                if c == "/":
                    slashes.append(i)

            pwd = pwd[:max(slashes)] + '/'
        elif path_to_change_to == "/":
            return '/'
        else:
            return pwd + path_to_change_to + '/'
        return pwd


class File:
    size: int
    name: str
    contents_size: int
    indexed: bool
    contents: list["File"]

    def __init__(self, name: str, pwd, file_size: int = 0, parent=None):
        self.name = name
        self.size = file_size
        self.contents = []
        self.parent = None
        self.contents_size = 0
        self.indexed = False
        self.pwd = pwd

    def add(self, file_to_add: "File"):
        self.contents.append(file_to_add)

    def size_of_dir(self):
        for c in self.contents:
            if c.size == 0:
                self.contents_size += c.contents_size
            else:
                self.contents_size += c.size

    def can_be_indexed(self):
        for c in self.contents:
            if c.size == 0 and c.contents_size == 0:
                return False
        return True


class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        """
        - / (dir)
          - a (dir)
            - e (dir)
              - i (file, size=584)
            - f (file, size=29116)
            - g (file, size=2557)
            - h.lst (file, size=62596)
          - b.txt (file, size=14848514)
          - c.dat (file, size=8504156)
          - d (dir)
            - j (file, size=4060174)
            - d.log (file, size=8033020)
            - d.ext (file, size=5626152)
            - k (file, size=7214296)"""
        pwd = "/"
        root = File("/", 0)
        current_folder = root
        listing = False
        files = []
        for line in input_to_use:
            if line.startswith("$"):
                # print("END LIST")
                listing = False
                data = line[2:].split(" ")
                if data[0] == "ls":
                    # print("START LIST")
                    listing = True
                elif data[0] == "cd":
                    pwd = Commands.change_directory(pwd, data[1])
                    if data[1] == "..":
                        current_folder = current_folder.parent

                    elif data[1] != "/":
                        temp = None
                        for f in current_folder.contents:
                            if f.name == data[1]:
                                temp = f

                        assert temp is not None
                        current_folder = temp
            if listing:
                if not line.startswith("$"):
                    data = line.split(" ")
                    if data[0] == 'dir':
                        temp = File(name=data[1], pwd=pwd, file_size=0, parent=current_folder)
                    else:
                        temp = File(name=data[1], pwd=pwd, file_size=int(data[0]), parent=current_folder)
                    files.append(temp)
                    temp.parent = current_folder
                    current_folder.add(temp)

        for f in files:
            print(f"{f.pwd}{f.name}")


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
    i.handle_raw_input(test_input)
