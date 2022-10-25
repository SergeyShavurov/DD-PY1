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
    sum_values_ = sum(dict_per.values())  # сумма всех значений
    dict_ = {}  # пустой словарь

    for key_, values_ in dict_per.items():  # вытаскиваем значения и ключи
        values_ = values_ / sum_values_ * 100  # перезаписываем значение
        dict_[key_] = values_  # записываем значение в словарь, в задании нет инфы касаемо округления, потому даны чистыe числа

    return dict_

print(get_percent_char(get_count_char(main_str)))

