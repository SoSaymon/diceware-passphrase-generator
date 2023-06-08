# IMPORTS
import random


def generate_numbers(number_of_numbers=5):
    num_arr = []
    i = 0
    while i < number_of_numbers:
        num = random.random()
        num *= 10
        num = round(num)
        if num > 6 or num < 1:
            continue
        num_arr.append(num)
        i += 1
    return num_arr


def concat_all_numbers(num_array):
    return ''.join(str(i) for i in num_array)


if __name__ == "__main__":
    print(concat_all_numbers(generate_numbers()))
