class Room:
    given_checksum: str
    built_checksum: str
    room_input: str
    sector_id: int
    decrypted_name: str

    def __init__(self, input_str: str):
        self.decrypted_name = ""
        self.given_checksum = input_str[-6:-1]
        self.room_input = input_str[:-11]
        self.sector_id = int(input_str[-10:-7])
        self.build_checksum()
        self.decrypt_name()

    def is_real(self):
        return self.built_checksum == self.given_checksum

    def build_checksum(self):
        """if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization."""
        letters_frequency = self.build_letter_frequency()
        max_used = max(letters_frequency.values())
        ordered_by_occurances = self.build_ordered_by_occurances(letters_frequency, max_used)
        alphabetized_ordered = self.alphabetize_ordered(ordered_by_occurances)
        self.built_checksum = self.transform_raw_into_built_checksum(alphabetized_ordered)

    def transform_raw_into_built_checksum(self, alphabetized_ordered):
        long_list = ""
        for chunk in alphabetized_ordered:
            long_list += "".join(chunk)
        return long_list[:5]

    def alphabetize_ordered(self, ordered_by_occurances):
        alphabetized_ordered = []
        for _ in ordered_by_occurances:
            _.sort()
            alphabetized_ordered.append(_)
        return alphabetized_ordered

    def build_ordered_by_occurances(self, letters_frequency, max_used):
        ordered_by_occurances = []
        for i in range(max_used, 0, -1):
            temp = []
            for k, v in letters_frequency.items():
                if v == i:
                    temp.append(k)
            ordered_by_occurances.append(temp)
        return ordered_by_occurances

    def build_letter_frequency(self):
        letters = [chr(e) for e in range(97, 97 + 26)]
        letters_frequency = dict()
        for c in self.room_input:
            if c in letters:
                if c not in letters_frequency.keys():
                    letters_frequency[c] = 0
                letters_frequency[c] += 1
        return letters_frequency

    def get_built_checksum(self):
        return self.built_checksum

    def get_sector_id(self):
        return self.sector_id

    def decrypt_name(self):
        decrypted_room_name = ""
        for c in self.room_input:
            decrypted_room_name += self.__decrypt_character(c)
        self.decrypted_name = decrypted_room_name

    def __decrypt_character(self,c):
        if c == "-":
            return " "
        else:
            current = ord(c)-97
            current += self.sector_id
            current = current % 26
            current += 97
            return chr(current)


class InputHandler:
    rooms: list[Room]

    def __init__(self):
        self.rooms = []

    def handle_raw_input(self, raw_input):
        lines = raw_input.split("\n")
        for line in lines:
            self.rooms.append(Room(line))


class OutputHandler:
    inputHandler: InputHandler
    output: int

    def __init__(self, i):
        self.inputHandler = i
        self.output = 0
        self.build_output()

    def build_output(self):
        for room in self.inputHandler.rooms:
            if room.is_real():
                if room.decrypted_name == "northpole object storage":
                    self.output = room.sector_id

    def get_output(self):
        return self.output