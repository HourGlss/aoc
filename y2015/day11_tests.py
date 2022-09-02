from day11 import increment_password, check_increasing_straight
from day11 import get_next_password, check_non_overlapping_pairs, check_password


def test_increment_password1():
    assert increment_password("xx", False, "") == "xy"


def test_increment_password2():
    assert increment_password("xz", False, "") == "ya"


def test_increment_password3():
    assert increment_password("ab", False, "") == "ac"


def test_increment_password4():
    assert increment_password("dzb", False, "") == "dzc"


def test_check_increasing_straight1():
    assert check_increasing_straight("zzabc") == True


def test_check_increasing_straight2():
    assert check_increasing_straight("zzabd") == False


def test_check_increasing_straight3():
    assert check_increasing_straight("abbceffg") == False


def test_check_increasing_straight4():
    assert check_increasing_straight("hijklmmn") == True


def test_check_non_overlapping_pairs1():
    assert check_non_overlapping_pairs("hijklmmn") == False


def test_check_non_overlapping_pairs2():
    assert check_non_overlapping_pairs("abbceffg") == True


def test_check_non_overlapping_pairs3():
    assert check_non_overlapping_pairs("abbcegjk") == False


def test_check_non_overlapping_pairs4():
    assert check_non_overlapping_pairs("abcdffaa") == True


def test_check_password():
    assert check_password("hijklmmn") == False
    assert check_password("abbceffg") == False
    assert check_password("abbcegjk") == False
    assert check_password("abcdffaa") == True
    assert check_password("ghjaabcc") == True


def test_get_next_password():
    assert get_next_password("abcdefgh") == "abcdffaa"


