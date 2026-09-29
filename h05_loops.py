"""Домашнее задание. Тема 5: циклы."""


def hw_15(n):
    """Первые n чисел Фибоначчи.

    Верните список первых n чисел Фибоначчи, начиная с 0 и 1:
    [0, 1, 1, 2, 3, 5, ...]. Для n == 0 верните пустой список, для n == 1 — [0].

    Примеры:
        hw_15(5) == [0, 1, 1, 2, 3]
        hw_15(1) == [0]
        hw_15(0) == []
        hw_15(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Генерируем первые n чисел Фибоначчи
    fib = [0, 1]
    while len(fib) < n:
        next_value = fib[-1] + fib[-2]
        fib.append(next_value)
    return fib[:n]


def hw_16(n):
    """Простое число.

    Верните True, если n — простое число (n >= 2, делится только на 1 и себя),
    иначе False. Реализуйте перебор делителей циклом до корня из n
    с выходом по break (или через for/else).

    Примеры:
        hw_16(0) == False
        hw_16(1) == False
        hw_16(2) == True
        hw_16(4) == False
        hw_16(97) == True
        hw_16(7919) == True
    """
    if n < 2:
        return False

    # Перебираем делители от 2 до корня из n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def hw_17(n):
    """FizzBuzz.

    Для чисел от 1 до n верните список строк:
      "fizzbuzz" — если число делится на 3 и на 5;
      "fizz"     — если делится только на 3;
      "buzz"     — если делится только на 5;
      иначе строковое представление числа.

    Примеры:
        hw_17(5) == ["1", "2", "fizz", "4", "buzz"]
        hw_17(15)[-1] == "fizzbuzz"
        hw_17(0) == []
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result