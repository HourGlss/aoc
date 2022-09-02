from day19_data import replacement_string_input, molecule_input


def break_string(input_str: str, break_start: int, break_end: int) -> tuple[str, str]:
    start = ""
    end = ""
    for i in range(len(input_str)):
        if i < break_start:
            start += input_str[i]
        if i > break_end:
            end += input_str[i]
    return start, end


def build_replacements(replacement_input: str):
    replacements_to_return = {}
    for replacement_line in [_.strip() for _ in replacement_input.split("\n")]:
        pieces = replacement_line.split(" ")
        if pieces[0] not in replacements_to_return.keys():
            replacements_to_return[pieces[0]] = []
        replacements_to_return[pieces[0]].append(pieces[2])
    return replacements_to_return


def combobulate_results(replacements_to_use: dict[str, list], molecule: str):
    results = set()
    total = 0
    for replacement in replacements_to_use.keys():
        lp = len(replacement)
        # print("---")
        for i in range(0, len(molecule)):
            if i + lp > len(molecule):
                break
            current = molecule[i:i+lp]
            # print(current)
            if current == replacement:
                for replace in replacements_to_use[replacement]:
                    s, e = break_string(molecule, i, i+lp-1)
                    test = f"{s}{replace}{e}"
                    # print(test)
                    results.add(test)
                    total += 1

    return len(results), total


if __name__ == "__main__":
    replacements = build_replacements(replacement_string_input)
    print(combobulate_results(replacements, molecule_input))
