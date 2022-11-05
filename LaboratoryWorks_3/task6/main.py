list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#print(list_numbers)

max_count = max(list_numbers) # максимальное значение
for index, count in enumerate(list_numbers): # получаем пары индекс - значение
    if count == max_count:
        list_numbers[-1], list_numbers[index] = list_numbers[index], list_numbers[-1] #присваивание индексов
print(list_numbers)

