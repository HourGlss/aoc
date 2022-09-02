from main import *


def test_inc():
    x = 0
    z = 10
    assert inc(x) == 1
    assert inc(z) == 11


def test_tpl():
    x = 0
    z = 1
    y = 3
    assert tpl(x) == 0
    assert tpl(z) == 3
    assert tpl(y) == 9


def test_hlf():
    x = 1
    y = 2
    z = 5
    assert hlf(x) == 0
    assert hlf(y) == 1
    assert hlf(z) == 2


def test_jmp():
    cmds = [['inc', 'a'],
            ['jio', 'a', '+2'],
            ['tpl', 'a'],
            ['inc', 'a'],
            ['inc', 'a'],
            ['jio', 'a', '+24'],
            ['tpl', 'a'],
            ['inc', 'a'],
            ["jmp", "-7"]
            ]
    _execution = 8
    offset = get_offset(cmds[8][1])
    assert offset == -7
    offset = get_offset(cmds[1][2])
    assert offset == 2
    offset = get_offset(cmds[5][2])
    assert offset == 24
    offset = get_offset(cmds[8][1])
    _execution = jmp(_execution, offset)
    assert _execution == 1


def test_jio():
    cmds = [['inc', 'a'],
            ['jio', 'a', '+2'],
            ['tpl', 'a'],
            ['inc', 'a'],
            ['inc', 'a'],
            ['jio', 'a', '+2'],
            ['tpl', 'a'],
            ['inc', 'a'],
            ["jmp", "-7"]
            ]
    _a = 0
    _execution = 0
    current_command = cmds[_execution]
    assert current_command == ['inc', 'a']
    _a = inc(_a)
    _execution = 1
    offset = get_offset(cmds[1][2])
    _execution = jio(_execution,offset,_a)
    assert _execution == 3

    _a = 0
    _execution = 0
    current_command = cmds[_execution]
    assert current_command == ['inc', 'a']
    _execution = 1
    offset = get_offset(cmds[1][2])
    _execution = jio(_execution, offset, _a)
    assert _execution == 2



