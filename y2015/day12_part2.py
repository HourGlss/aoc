import time

lowers = [chr(e) for e in range(97, 97 + 26)]


def convert_number_to_letters(input_int: int) -> str:
    global lowers
    return_string = ""
    for c in str(input_int):
        return_string += lowers[int(c)]
    return return_string


def find_numbers_in_list(input_list: list) -> tuple[list[int], list[list | dict | str]]:
    return_useful_list = []
    return_non_used_with_substitutions = []
    for e in input_list:
        if isinstance(e, int):
            return_useful_list.append(e)
            return_non_used_with_substitutions.append("z")
        else:
            return_non_used_with_substitutions.append(e)
    return return_useful_list, return_non_used_with_substitutions


total_list = []


def recursive_teardown(current_input: list | dict):
    # print("curr",current_input)
    global total_list
    if isinstance(current_input, dict):
        useful, not_useful = find_numbers_in_dict(current_input)
        total_list += useful
        for top_k, top_v in not_useful.items():
            if isinstance(top_v, dict):
                useful, not_useful = find_numbers_in_dict(top_v)
                total_list += useful
                recursive_teardown(not_useful)
            elif isinstance(top_v, list):
                useful, not_useful = find_numbers_in_list(top_v)
                total_list += useful
                for top_e in not_useful:
                    recursive_teardown(top_e)
    elif isinstance(current_input, list):
        useful, not_useful = find_numbers_in_list(current_input)
        total_list += useful
        for top_e in not_useful:
            if isinstance(top_e, list) or isinstance(top_e, dict):
                recursive_teardown(top_e)


def find_numbers_in_dict(input_dict: dict) -> tuple[list[int], dict]:
    found = False
    for k, v in input_dict.items():
        if k == "red":
            found = True
        if v == "red":
            found = True
    if found:
        return [], {}
    return_filtered_dict = {}
    return_list = []
    for k, v in input_dict.items():
        if isinstance(v, int):
            return_list.append(v)
            v = "z"
        return_filtered_dict[k] = v

    return return_list, return_filtered_dict


def add_numbers_in_list(input_list: list) -> int:
    return sum(input_list)


if __name__ == "__main__":
    from day12_data import data

    recursive_teardown(data)
    # print(total_list)
    print(add_numbers_in_list(total_list))
