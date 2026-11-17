"""Домашнее задание. Тема 4: миксины и MRO."""


class DescribeMixin:
    """Задание 11. Строковое описание объекта.

    Метод describe() возвращает "ClassName: имя1=значение1, имя2=значение2"
    по всем атрибутам экземпляра (self.__dict__), имя класса — через
    type(self).__name__.

    Примеры:
        class Point(DescribeMixin):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        Point(1, 2).describe() == "Point: x=1, y=2"
    """

    def describe(self):
        raise NotImplementedError("Реализуйте DescribeMixin.describe")


class EqMixin:
    """Задание 12. Сравнение по полям (шаблонный метод).

    Класс-носитель реализует fields() — кортеж ИМЁН атрибутов для
    сравнения. Миксин определяет __eq__(other): True, только если other —
    экземпляр того же класса и все поля совпадают.

    Класс Book(title, author) наследует EqMixin, fields() → ("title", "author").

    Примеры:
        Book("а", "X") == Book("а", "X")
        Book("а", "X") != Book("б", "X")
        Book("а", "X") == "а"   # False: другой тип
    """

    def fields(self):
        raise NotImplementedError("Носитель миксина должен реализовать fields()")

    def __eq__(self, other):
        raise NotImplementedError("Реализуйте EqMixin.__eq__")


class Book(EqMixin):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def fields(self):
        raise NotImplementedError("Реализуйте Book.fields")


class P:
    """Задание 13. Ромб MRO: S→Q→R→P.

    Четыре класса: P; Q(P); R(P); S(Q, R). Метод who(): P возвращает "P";
    каждый следующий — "{буква}->" плюс super().who(). MRO класса S
    даёт порядок обхода S → Q → R → P.

    Примеры:
        P().who() == "P"
        Q().who() == "Q->P"
        R().who() == "R->P"
        S().who() == "S->Q->R->P"
    """

    def who(self):
        raise NotImplementedError("Реализуйте P.who")


class Q(P):
    def who(self):
        raise NotImplementedError("Реализуйте Q.who")


class R(P):
    def who(self):
        raise NotImplementedError("Реализуйте R.who")


class S(Q, R):
    def who(self):
        raise NotImplementedError("Реализуйте S.who")


class StatsMixin:
    """Задание 14. Ленивое состояние в миксине (без __init__).

    Метод remember(value) при первом вызове создаёт список _log
    и добавляет значение. Метод average() возвращает среднее по _log
    (float) или 0, если запоминаний ещё не было.

    Примеры:
        class Sensor(StatsMixin):
            def __init__(self, name):
                self.name = name

        s = Sensor("датчик")
        s.average() == 0
        s.remember(2); s.remember(4)
        s.average() == 3.0
        s2 = Sensor("другой")
        s2.average() == 0        # состояние независимое
    """

    def remember(self, value):
        raise NotImplementedError("Реализуйте StatsMixin.remember")

    def average(self):
        raise NotImplementedError("Реализуйте StatsMixin.average")
