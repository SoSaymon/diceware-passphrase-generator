import sys

sys.path.append("/home/sosaymon/Projects/diceware-password-generator/")

from passgen import find_index, get_word


def test_find_index():
    wordlist = [
        {"number": "1", "word": "a"},
        {"number": "2", "word": "b"},
        {"number": "3", "word": "c"},
    ]
    assert find_index(wordlist, "1") == 0
    assert find_index(wordlist, "2") == 1
    assert find_index(wordlist, "3") == 2
    assert find_index(wordlist, "4") == -1


def test_get_word():
    assert get_word([{"word": "a"}], 0) == "a"
