from enum import Enum


class ValidCommands(Enum):
    INC = 0
    TPL = 1
    HLF = 2
    JMP = 3
    JIE = 4
    JIO = 5


def tpl(register: int) -> int:
    return int(register * 3)


def hlf(register: int) -> int:
    return register >> 1


def inc(register: int) -> int:
    return register + 1


def jmp(current_index: int, offset: int) -> int:
    return current_index + offset


def jie(current_index: int, offset: int, register: int) -> int:
    if register % 2 == 0:
        return jmp(current_index, offset)
    return current_index + 1


def jio(current_index: int, offset: int, register: int) -> int:
    if register == 1:
        return jmp(current_index, offset)
    return current_index + 1


def main(_commands: list[tuple[ValidCommands, str | None, int | None]], start_a: int = None, start_b: int = None) -> \
        tuple[int, int]:
    if start_a is not None:
        _a = start_a
    else:
        _a = 0
    if start_b is not None:
        _b = start_b
    else:
        _b = 0
    execution = 0
    while True:
        if execution >= len(_commands):
            break
        current_command, register_to_use, offset = _commands[execution]
        jump = False
        if current_command == ValidCommands.INC:
            if register_to_use == 'a':
                _a = inc(_a)
            elif register_to_use == 'b':
                _b = inc(_b)
        elif current_command == ValidCommands.TPL:
            if register_to_use == 'a':
                _a = tpl(_a)
            elif register_to_use == 'b':
                _b = tpl(_b)
        elif current_command == ValidCommands.HLF:
            if register_to_use == 'a':
                _a = hlf(_a)
            elif register_to_use == 'b':
                _b = hlf(_b)
        elif current_command == ValidCommands.JMP:
            jump = True
            execution = jmp(execution, offset)
        elif current_command == ValidCommands.JIE:
            jump = True
            if register_to_use == 'a':
                execution = jie(execution, offset, _a)
            elif register_to_use == 'b':
                execution = jie(execution, offset, _b)
        elif current_command == ValidCommands.JIO:
            jump = True
            if register_to_use == 'a':
                execution = jio(execution, offset, _a)
            elif register_to_use == 'b':
                execution = jio(execution, offset, _b)

        if not jump:
            execution += 1
    return _a, _b


def get_offset(current_cmd_str: str) -> int:
    direction = current_cmd_str[0]
    actual = None
    if direction == "+":
        actual = 1
    else:
        actual = -1
    scale = int(current_cmd_str[1:])
    offset = int(scale * actual)
    return offset


def seperate_list(raw_data: str) -> list[list[str]]:
    _commands = []

    for line in [_.strip() for _ in raw_data.split("\n")]:
        _commands.append(line.split(" "))
    return _commands


def machine(bad_list: list[list[str]]) -> list[tuple[ValidCommands, str | None, int | None]]:
    good_list = []
    for e in bad_list:
        if e[0] == "inc":
            if e[1] == 'a':
                good_list.append((ValidCommands.INC, "a", None))
            elif e[1] == 'b':
                good_list.append((ValidCommands.INC, "b", None))
            else:
                assert ValueError
        elif e[0] == "tpl":
            if e[1] == 'a':
                good_list.append((ValidCommands.TPL, "a", None))
            elif e[1] == 'b':
                good_list.append((ValidCommands.TPL, "b", None))
            else:
                assert ValueError
        elif e[0] == 'hlf':
            if e[1] == 'a':
                good_list.append((ValidCommands.HLF, "a", None))
            elif e[1] == 'b':
                good_list.append((ValidCommands.HLF, "b", None))
            else:
                assert ValueError
        elif e[0] == 'jmp':
            offset = get_offset(e[1])
            good_list.append((ValidCommands.JMP, None, offset))
        elif e[0] == 'jie':
            offset = get_offset(e[2])
            if e[1] == 'a':
                good_list.append((ValidCommands.JIE, 'a', offset))
            elif e[1] == 'b':
                good_list.append((ValidCommands.JIE, 'b', offset))
            else:
                assert ValueError
        elif e[0] == 'jio':
            offset = get_offset(e[2])
            if e[1] == 'a':
                good_list.append((ValidCommands.JIO, 'a', offset))
            elif e[1] == 'b':
                good_list.append((ValidCommands.JIO, 'b', offset))
            else:
                assert ValueError
        else:
            assert ValueError

    return good_list


# if __name__ == "__main__":
#     import data
#
#     bad_commands = seperate_list(data.real)
#     usable_commands = machine(bad_commands)
#     a, b = main(usable_commands, start_a=1, start_b=0)
#     print(a, b)
