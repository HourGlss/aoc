from day19 import *


def test_build_replacements():
    replace_string = """H => HO
    H => OH
    O => HH"""
    replacements = build_replacements(replace_string)
    assert replacements == {"H": ["HO", "OH"], "O": ["HH"]}


def test_simple():
    replace_string = """H => HO
H => OH
O => HH"""
    replacements = build_replacements(replace_string)
    molecule = "HOH"
    assert combobulate_results(replacements, molecule) == (4, 5)


def test_medium():
    replace_string = """H => HO
    H => OH
    O => HH"""
    replacements = build_replacements(replace_string)
    molecule = "HOHOHO"
    assert combobulate_results(replacements, molecule) == (7, 9)


def test_other_char():
    replacement_string = "H => OO"
    molecule = "H2O"
    replacements = build_replacements(replacement_string)
    useful, _ = combobulate_results(replacements, molecule)
    assert useful == 1

def test_multichar_keys():
    replacement_string = """az => XX
    az => XY"""
    molecule = "azb"
    replacements = build_replacements(replacement_string)
    assert combobulate_results(replacements, molecule) == (2, 2)

