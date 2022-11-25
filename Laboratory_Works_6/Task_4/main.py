import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=',', new_line='\n') -> list[dict]:
    # считываем текст
    with open(filename) as f:
        text = f.read().strip()

    # делим на части
    rows = []
    text_lines = text.split(new_line)
    for text_line in text_lines:
        row = text_line.split(delimiter)
        rows.append(row)

    if len(rows) <= 0:  # пустой файл
        return []

    # выделяем заголовки
    headers = rows.pop(0)

    # формируем ответ
    result = []
    for row in rows:
        line = dict(zip(headers, row))
        result.append(line)

    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))