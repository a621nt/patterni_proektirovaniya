"""Домашнее задание. Тема 6: композиция вместо наследования."""

from abc import ABC, abstractmethod


class TextTransformer:
    """Задание 18. Цепочка правил (композиция функций).

    Конструктор принимает rules — список функций str → str. Метод
    apply(text) прогоняет текст через правила ПО ПОРЯДКУ и возвращает
    результат последнего преобразования.

    Примеры:
        t = TextTransformer([str.upper, lambda s: s.replace(" ", "_")])
        t.apply("hello world") == "HELLO_WORLD"
        TextTransformer([]).apply("как есть") == "как есть"
    """

    def __init__(self, rules):
        raise NotImplementedError("Реализуйте TextTransformer.__init__")

    def apply(self, text):
        raise NotImplementedError("Реализуйте TextTransformer.apply")


class PaymentMethod(ABC):
    """Задание 19. Методы оплаты: стратегии за общим интерфейсом.

    Абстрактный pay(amount) → строка. Реализации:
      CardMethod: "оплачено картой {amount}"
      CashMethod: "оплачено наличными {amount}"
    Checkout(method).pay(amount) делегирует вызов методу оплаты.

    Примеры:
        Checkout(CardMethod()).pay(100) == "оплачено картой 100"
        Checkout(CashMethod()).pay(250) == "оплачено наличными 250"
    """

    @abstractmethod
    def pay(self, amount):
        raise NotImplementedError("Реализуйте PaymentMethod.pay")


class CardMethod(PaymentMethod):
    def pay(self, amount):
        raise NotImplementedError("Реализуйте CardMethod.pay")


class CashMethod(PaymentMethod):
    def pay(self, amount):
        raise NotImplementedError("Реализуйте CashMethod.pay")


class Checkout:
    def __init__(self, method):
        raise NotImplementedError("Реализуйте Checkout.__init__")

    def pay(self, amount):
        raise NotImplementedError("Реализуйте Checkout.pay")


class Sword:
    """Задание 20. Персонаж со сменным оружием.

    Sword.attack() → "удар мечом"; Bow.attack() → "выстрел из лука".
    Character(name, weapon): attack() возвращает "{name}: {атака оружия}";
    set_weapon(weapon) меняет оружие на ходу.

    Примеры:
        hero = Character("Ратибор", Sword())
        hero.attack() == "Ратибор: удар мечом"
        hero.set_weapon(Bow())
        hero.attack() == "Ратибор: выстрел из лука"
    """

    def attack(self):
        raise NotImplementedError("Реализуйте Sword.attack")


class Bow:
    def attack(self):
        raise NotImplementedError("Реализуйте Bow.attack")


class Character:
    def __init__(self, name, weapon):
        raise NotImplementedError("Реализуйте Character.__init__")

    def set_weapon(self, weapon):
        raise NotImplementedError("Реализуйте Character.set_weapon")

    def attack(self):
        raise NotImplementedError("Реализуйте Character.attack")
