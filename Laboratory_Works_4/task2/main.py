def get_count_char(str_):
    str_lower_ = str_.lower()
    dict_ = {}  # пустой словарь для работы в цикле for

    for char_ in str_lower_:  # цикл идет по всем символам строки
        if char_.isalpha():  # проверка на букву
            dict_[char_] = dict_.get(char_, 0) + 1  # запись  в словарь,

    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_percent_char(dict_per): # пятый пункт задания Функция нахождения процента содержания каждого элемента
    sum_values = sum(dict_per.values())  # сумма всех значений
    dict = {}  # пустой словарь

    for key, value in dict_per.items():  # вытаскиваем значения и ключи
        value = round(value / sum_values * 100, 2) # перезаписываем значение округленные до 2 знака
        dict[key] = value

    return dict

print(get_percent_char(get_count_char(main_str)))

