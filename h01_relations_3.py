"""Домашнее задание. Тема 1: инкапсуляция и отношения."""


class Safe:
    """Задание 01. Сейф: приватность и счётчик попыток.

    Конструктор принимает код code. Внутренности храните с двойным
    подчёркиванием (name mangling). Метод open(code): верный код —
    возвращает "открыто"; неверный — ValueError("неверный код") и
    увеличивает защищённый счётчик _attempts. Свойство attempts
    возвращает число неудачных попыток.

    Примеры:
        s = Safe(777)
        s.open(777) == "открыто"
        s.attempts == 0
        s.open(111)  # ValueError: неверный код
        s.attempts == 1
        hasattr(s, "__code") == False
    """

    def __init__(self, code):
        raise NotImplementedError("Реализуйте Safe.__init__")

    def open(self, code):
        raise NotImplementedError("Реализуйте Safe.open")

    @property
    def attempts(self):
        raise NotImplementedError("Реализуйте Safe.attempts")


class Config:
    """Задание 02. Настройки только для чтения.

    Конструктор принимает произвольные именованные настройки (**settings)
    и хранит их во внутреннем словаре. Свойство settings возвращает словарь
    (можно копию) и НЕ имеет сеттера. Изменения — только через метод
    update(key, value); метод get(key, default=None) читает значение.

    Примеры:
        c = Config(theme="dark", lang="ru")
        c.settings == {"theme": "dark", "lang": "ru"}
        c.get("theme") == "dark"
        c.get("missing", 0) == 0
        c.update("lang", "en")
        c.get("lang") == "en"
        c.settings = {}   # AttributeError
    """

    def __init__(self, **settings):
        raise NotImplementedError("Реализуйте Config.__init__")

    @property
    def settings(self):
        raise NotImplementedError("Реализуйте Config.settings")

    def update(self, key, value):
        raise NotImplementedError("Реализуйте Config.update")

    def get(self, key, default=None):
        raise NotImplementedError("Реализуйте Config.get")


class Player:
    """Задание 03, часть 1. Игрок."""

    def __init__(self, name):
        self.name = name


class Team:
    """Задание 03, часть 2. Агрегация: команда из игроков.

    add(player) запоминает игрока; roster() возвращает имена в порядке
    добавления. Игроки создаются снаружи и остаются теми же объектами.

    Примеры:
        t = Team("звёзды")
        anna = Player("Анна")
        t.add(anna)
        t.roster() == ["Анна"]
        t.add(Player("Борис"))
        t.roster() == ["Анна", "Борис"]
    """

    def __init__(self, name):
        raise NotImplementedError("Реализуйте Team.__init__")

    def add(self, player):
        raise NotImplementedError("Реализуйте Team.add")

    def roster(self):
        raise NotImplementedError("Реализуйте Team.roster")


class Course:
    """Задание 04. Ассоциация: курс и записавшиеся студенты.

    enroll(student) добавляет студента; students() возвращает имена
    в порядке записи. У студента есть атрибут name.

    Примеры:
        c = Course("Python")
        c.enroll(Student("Анна"))
        c.enroll(Student("Борис"))
        c.students() == ["Анна", "Борис"]
    """

    def __init__(self, title):
        raise NotImplementedError("Реализуйте Course.__init__")

    def enroll(self, student):
        raise NotImplementedError("Реализуйте Course.enroll")

    def students(self):
        raise NotImplementedError("Реализуйте Course.students")


class Student:
    """Студент (для задания 04)."""

    def __init__(self, name):
        self.name = name
