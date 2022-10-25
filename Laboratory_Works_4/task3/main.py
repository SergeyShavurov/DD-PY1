def delete(list_, index=None):
    if index != None:  # если индекс  задан то удаляем его
        new_list_ = list_[: index] # промежуточный лист
        list_ = new_list_ + list_[index + 1:]
        return list_

    else:  # если индекс не задан то удаляем последний элемент
        list_ = list_[:-1]
        return list_
        # Была мысль сделать через List_.pop(index) как лучше?

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]