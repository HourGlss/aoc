class PasswordBuilder:
    password: str

    def __init__(self, raw_data):
        column_data = PasswordBuilder.__seperate_data_from_columns(raw_data)
        self.password = ""
        for column in column_data:
            self.password += PasswordBuilder.get_lowest_occurance_char_in_list(column)

    @staticmethod
    def __seperate_data_from_columns(raw_data):
        lines = raw_data.split('\n')
        rows = []
        for i in range(len(lines[0])):
            rows.append([])
        for line in lines:
            for i, c in enumerate(line):
                rows[i].append(c)
        return rows

    @staticmethod
    def get_lowest_occurance_char_in_list(list_data) -> str:
        letters = dict()
        for c in list_data:
            if c not in letters.keys():
                letters[c] = 0
            letters[c] += 1
        min_used = min(letters.values())
        for k, v in letters.items():
            if v == min_used:
                return k


if __name__ == "__main__":
    from y2016.day6.data import test_input

    p = PasswordBuilder(test_input)
