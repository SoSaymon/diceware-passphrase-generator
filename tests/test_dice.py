from dice import generate_numbers, concat_all_numbers, generate_string_of_numbers


def test_generate_numbers():
    assert len(generate_numbers()) == 5
    assert len(generate_numbers(10)) == 10
    assert len(generate_numbers(0)) == 0
    assert len(generate_numbers(-1)) == 0

    assert all([i in range(1, 7) for i in generate_numbers()])
    assert all([i in range(1, 7) for i in generate_numbers(10)])
    assert all([i in range(1, 7) for i in generate_numbers(0)])
    assert all([i in range(1, 7) for i in generate_numbers(-1)])


def test_concat_all_numbers():
    result = concat_all_numbers([1, 2, 3, 4, 5])
    assert result == '12345'

    result = concat_all_numbers([1, 2, 3, 4, 5, 6])
    assert result == '123456'


def test_generate_string_of_numbers():
    result = generate_string_of_numbers(5)
    assert len(result) == 5
    for char in result:
        assert "1" <= char <= "6"


def test_dice():
    test_generate_numbers()
    test_concat_all_numbers()
    test_generate_string_of_numbers()
    

if __name__ == '__main__':
    test_dice()
