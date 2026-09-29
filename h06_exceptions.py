"""Домашнее задание. Тема 6: ошибки и исключения."""


def hw_18(text):
    """Разбор пары чисел из строки.

    Строка должна содержать два целых числа, разделённых пробелом, например "3 4".
    Верните кортеж из двух чисел. Если строка не подходит (одно число,
    три числа, не числа), перехватите ошибку преобразования и верните None.

    Примеры:
        hw_18("3 4") == (3, 4)
        hw_18("-1 10") == (-1, 10)
        hw_18("3") is None
        hw_18("3 x") is None
        hw_18("1 2 3") is None
    """
    words = text.split()

    # Должно быть ровно два слова
    if len(words) != 2:
        return None

    try:
        # Преобразуем оба слова в целые числа
        num1 = int(words[0])
        num2 = int(words[1])
        return (num1, num2)
    except ValueError:
        return None


def hw_19(path):
    """Чтение файла в список строк.

    Верните список строк файла по пути path (без завершающих переводов строк).
    Используйте конструкцию with. Если файла не существует, перехватите
    FileNotFoundError и верните пустой список [].

    Примеры (файл со строками "раз\\nдва\\nтри"):
        hw_19(<путь>) == ["раз", "два", "три"]
        hw_19(<несуществующий путь>) == []
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            # Читаем все строки и убираем завершающие переносы строк
            lines = [line.rstrip('\n\r') for line in file.readlines()]
            return lines
    except FileNotFoundError:
        return []


def hw_20(age):
    """Валидация возраста.

    Верните age, если значение корректно. Иначе выбросьте исключение:
      - TypeError("возраст должен быть целым числом") — если age не int
        (например, строка или float);
      - ValueError("возраст должен быть от 0 до 120") — если age < 0 или age > 120.

    Примеры:
        hw_20(30) == 30
        hw_20(0) == 0
        hw_20(120) == 120
        pytest.raises(TypeError): hw_20("30")
        pytest.raises(TypeError): hw_20(12.0)
        pytest.raises(ValueError): hw_20(-1)
        pytest.raises(ValueError): hw_20(121)
    """
    # Проверяем тип — должен быть int
    if not isinstance(age, int):
        raise TypeError("возраст должен быть целым числом")

    # Проверяем диапазон — от 0 до 120
    if age < 0 or age > 120:
        raise ValueError("возраст должен быть от 0 до 120")

    return age