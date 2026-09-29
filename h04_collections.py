"""Домашнее задание. Тема 4: коллекции."""


def hw_11(text):
    """Самое частое слово.

    Верните слово, которое встречается в строке text чаще всего
    (разделители — пробельные символы). При равенстве частот верните
    то слово, которое встретилось в строке раньше.

    Примеры:
        hw_11("кот пёс кот кот пёс") == "кот"
        hw_11("а б а б") == "а"
        hw_11("один") == "один"
    """
    words = text.split()
    frequency = {}

    # Считаем частоту каждого слова
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Находим слово с максимальной частотой
    # Если несколько слов имеют одинаковую частоту, возвращаем первое
    most_frequent = None
    max_count = -1

    for word, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = word

    return most_frequent


def hw_12(matrix):
    """Суммы строк матрицы.

    matrix — список списков чисел. Верните список, где i-й элемент —
    сумма элементов i-й строки matrix.

    Примеры:
        hw_12([[1, 2], [3, 4]]) == [3, 7]
        hw_12([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [6, 15, 24]
        hw_12([]) == []
        hw_12([[10]]) == [10]
    """
    result = []
    for row in matrix:
        row_sum = sum(row)
        result.append(row_sum)
    return result


def hw_13(items):
    """Убрать дубликаты, сохранив порядок.

    Верните новый список, содержащий элементы items в порядке первого
    вхождения, без повторов. Элементы можно считать хешируемыми.

    Примеры:
        hw_13([1, 2, 1, 3, 2]) == [1, 2, 3]
        hw_13(["a", "b", "a", "a"]) == ["a", "b"]
        hw_13([]) == []
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def hw_14(mapping):
    """Инвертировать словарь.

    Поменяйте местами ключи и значения: верните словарь, где ключи —
    значения mapping, а значения — ключи. Все значения mapping можно
    считать уникальными и хешируемыми.

    Примеры:
        hw_14({"a": 1, "b": 2}) == {1: "a", 2: "b"}
        hw_14({}) == {}
        hw_14({"x": (1, 2)}) == {(1, 2): "x"}
    """
    inverted = {}
    for key, value in mapping.items():
        inverted[value] = key
    return inverted