from pprint import pprint


def list_with_dictionaries_of_numbers(number_of_iterations) -> list[dict]:  # функция принимает количество итераций, зачем то использовал анотацию (раз научился, почему бы и нет)
    list_dictionaries = []  # пустой словарь для записи в for
    for i in range(number_of_iterations + 1):  # +1 используется для удобства так как, range формирует последовательность не включая окончание
        dict_number = {'bin': bin(i), 'oct': oct(i), 'dec': i, 'hex': hex(i)}  # формирование словаря
        list_dictionaries.append(dict_number)  # запись словаря в список
    return (list_dictionaries)


pprint(list_with_dictionaries_of_numbers(15))
