from random import randint

def get_unique_list_numbers(list_length = 15):

    unique_list_numbers = []

    while len(unique_list_numbers) < list_length:
        x = randint(-10, 10)
        if x not in unique_list_numbers:
            unique_list_numbers.append(x)

    return unique_list_numbers

print(get_unique_list_numbers())