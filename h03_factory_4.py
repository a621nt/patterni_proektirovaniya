"""Домашнее задание. Тема 3: фабрики."""


class SQLiteConnection:
    """Продукт: SQLite-соединение."""

    def connect(self):
        return "sqlite: подключено"


class PostgresConnection:
    def connect(self):
        return "postgres: подключено"


def hw_08(kind):
    """Фабрика соединений.

    "sqlite" → SQLiteConnection, "postgres" → PostgresConnection.
    Неизвестный kind — ValueError("неизвестная база").

    Примеры:
        hw_08("sqlite").connect() == "sqlite: подключено"
        isinstance(hw_08("postgres"), PostgresConnection)
        hw_08("oracle")  # ValueError: неизвестная база
    """
    mapping = {"sqlite": SQLiteConnection, "postgres": PostgresConnection}
    if kind not in mapping:
        raise ValueError("неизвестная база")
    return mapping[kind]()


class Dog2:
    """Продукт для задания 09."""

    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name}: гав"


class Cat2:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f"{self.name}: мяу"


class AnimalFactory:
    """Задание 09. Фабрика животных.

    Классовый метод create(kind, name): "dog" → Dog2(name), "cat" → Cat2(name).
    Неизвестный kind — ValueError("неизвестное животное").

    Примеры:
        AnimalFactory.create("dog", "Рекс").sound() == "Рекс: гав"
        isinstance(AnimalFactory.create("cat", "Мурка"), Cat2)
    """

    @classmethod
    def create(cls, kind, name):
        if kind == "dog":
            return Dog2(name)
        elif kind == "cat":
            return Cat2(name)
        else:
            raise ValueError("неизвестное животное")


class CsvReport:
    """Продукт для задания 10."""

    def render(self, rows):
        return ";".join(str(r) for r in rows)


class JsonReport:
    def render(self, rows):
        return "{" + ", ".join(f'"{i}": {v}' for i, v in enumerate(rows)) + "}"


def hw_10(fmt):
    """Фабрика отчётов.

    "csv" → CsvReport, "json" → JsonReport. Неизвестный формат —
    ValueError("неизвестный формат").

    Примеры:
        hw_10("csv").render([1, 2]) == "1;2"
        hw_10("json").render([7, 9]) == '{"0": 7, "1": 9}'
    """
    if fmt == "csv":
        return CsvReport()
    elif fmt == "json":
        return JsonReport()
    else:
        raise ValueError("неизвестный формат")
