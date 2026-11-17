"""Домашнее задание. Тема 2: Singleton."""


class Capital:
    """Задание 05. Синглтон со сменой имени.

    Синглтон. Атрибут name изначально "не установлен"; метод rename(new_name)
    меняет имя — и это видно через любой вызов класса.

    Примеры:
        Capital() is Capital()
        Capital().name == "не установлен"
        Capital().rename("Пермь")
        Capital().name == "Пермь"
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = "не установлен"
        return cls._instance

    def rename(self, new_name):
        self.name = new_name


class Fibonacci:
    """Задание 06. Синглтон-генератор чисел Фибоначчи.

    Метод next() выдаёт очередное число последовательности: 0, 1, 1, 2, 3, 5, ...
    Состояние общее для всех «экземпляров». Не забудьте защиту от
    повторного __init__.

    Примеры:
        Fibonacci() is Fibonacci()
        a = Fibonacci()
        a.next() == 0
        a.next() == 1
        Fibonacci().next() == 1
        Fibonacci().next() == 2
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_a"):
            self._a, self._b = 0, 1

    def next(self):
        res = self._a
        self._a, self._b = self._b, self._a + self._b
        return res


class God:
    """Задание 07. Синглтон со счётчиком обращений.

    Синглтон. Классовый метод prayers() возвращает, сколько раз вызывался
    pray() (у любого «экземпляра» — счётчик общий).

    Примеры:
        God() is God()
        God.prayers() == 0
        God().pray()
        God().pray()
        God.prayers() == 2
    """

    _instance = None
    _prayers = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pray(self):
        God._prayers += 1

    @classmethod
    def prayers(cls):
        return cls._prayers
