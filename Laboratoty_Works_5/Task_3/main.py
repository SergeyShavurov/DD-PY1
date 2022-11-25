from random import randint, shuffle

def get_unique_list_numbers(list_length = 15) -> list[int]:
    set_of_numbers = set()
    while len(set_of_numbers) < list_length:
        set_of_numbers.add(randint(-10, 10))

    unique_list_numbers = list(set_of_numbers)
    shuffle(unique_list_numbers) # если не использоват перемешивание, то значения упорядочиваются

    return unique_list_numbers

print(get_unique_list_numbers())
