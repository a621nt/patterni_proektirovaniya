"""Домашнее задание. Тема 5: абстрактные классы."""

from abc import ABC, abstractmethod


class SoundSource(ABC):
    """Задание 15. Шаблонный метод на абстрактной базе.

    Абстрактный make_sound(); конкретный speak(times=1) возвращает
    звуки, разделённые пробелами: make_sound() ровно times раз.
    Подкласс DogSound: make_sound() → "гав".

    Примеры:
        DogSound().speak() == "гав"
        DogSound().speak(3) == "гав гав гав"
        SoundSource()   # TypeError
    """

    @abstractmethod
    def make_sound(self):
        raise NotImplementedError("Реализуйте SoundSource.make_sound")

    def speak(self, times=1):
        raise NotImplementedError("Реализуйте SoundSource.speak")


class DogSound(SoundSource):
    def make_sound(self):
        raise NotImplementedError("Реализуйте DogSound.make_sound")


class Storage(ABC):
    """Задание 16, часть 1. Интерфейс хранилища.

    Абстрактные save(key, value) и load(key). Реализуйте MemoryStorage
    на словаре: load несуществующего ключа возвращает None.

    Примеры:
        st = MemoryStorage()
        st.save("a", 1)
        st.load("a") == 1
        st.load("нет") is None
    """

    @abstractmethod
    def save(self, key, value):
        raise NotImplementedError("Реализуйте Storage.save")

    @abstractmethod
    def load(self, key):
        raise NotImplementedError("Реализуйте Storage.load")


class MemoryStorage(Storage):
    def save(self, key, value):
        raise NotImplementedError("Реализуйте MemoryStorage.save")

    def load(self, key):
        raise NotImplementedError("Реализуйте MemoryStorage.load")


class Sealed:
    """Задание 17. Запрет наследования.

    Реализуйте класс Sealed так, чтобы ЛЮБАЯ попытка унаследоваться от него
    возбуждала TypeError при определении подкласса. Подсказка: метод
    __init_subclass__. Сам Sealed должен спокойно создаваться.

    Примеры:
        Sealed()          # работает
        class Child(Sealed): pass   # TypeError
    """

    def __init_subclass__(cls, **kwargs):
        raise NotImplementedError("Реализуйте Sealed.__init_subclass__")
