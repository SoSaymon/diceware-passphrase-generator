import pytest
from wordlist_loader import load_wordlist, make_dict, make_wordlist, load_lines_from_file


def test_load_wordlist():
    assert load_wordlist("test_wordlist.txt") == ['1   one\n', '2   two\n', '3   three']


def test_make_dict():
    assert make_dict("1   one\n") == {"number": "1", "word": "one"}


def test_make_wordlist():
    assert make_wordlist(['1   one\n', '2   two\n', '3   three']) == [
        {"number": "1", "word": "one"},
        {"number": "2", "word": "two"},
        {"number": "3", "word": "three"}
    ]


def test_wordlist_maker():
    assert load_lines_from_file("test_wordlist.txt") == [
        {"number": "1", "word": "one"},
        {"number": "2", "word": "two"},
        {"number": "3", "word": "three"}
    ]


def test_wordlist_maker_exceptions():
    with pytest.raises(FileNotFoundError):
        load_lines_from_file("nonexistent_file.txt")


def test_wordlist_loader():
    test_load_wordlist()
    test_wordlist_maker_exceptions()
    test_make_dict()
    test_make_wordlist()
    test_wordlist_maker()


if __name__ == '__main__':
    test_wordlist_loader()
