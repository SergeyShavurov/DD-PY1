src = not False and True or False and not True

result = True and True or False and False # Избавляемся от отрицания not
result = True or False # Избавляемся от and
result = True # избавляемся от or

print(src == result)
