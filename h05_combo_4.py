"""Домашнее задание. Тема 5: порождающие вместе."""


class Settings:
    """Задание 15. Синглтон с настройками по умолчанию.

    Синглтон: все вызовы Settings() — один объект. При первом создании
    словарь настроек наполняется значениями по умолчанию:
    {"тема": "светлая", "язык": "ru"}. Методы set(key, value) и
    get(key, default=None) — общие для всего приложения.

    Примеры:
        Settings() is Settings()
        Settings().get("тема") == "светлая"
        Settings().set("тема", "тёмная")
        Settings().get("тема") == "тёмная"
        Settings().get("нет", 0) == 0
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {"тема": "светлая", "язык": "ru"}
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)


def hw_16(func):
    """Задание 16. Фабрика считающих обёрток.

    Верните обёртку, которая считает свои вызовы в атрибуте calls
    (изначально 0) и пробрасывает результат func.

    Примеры:
        calls = []
        def side_effect(x):
            calls.append(x)
            return x + 1

        wrapped = hw_16(side_effect)
        wrapped.calls == 0
        wrapped(1) == 2
        wrapped(2) == 3
        wrapped.calls == 2
        calls == [1, 2]
    """
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


class Cache:
    """Задание 17. Синглтон-кэш.

    Синглтон с общим кэшем: put(key, value) сохраняет; get(key) возвращает
    значение или None. Кэш один для всего приложения (защита от повторного
    __init__ обязательна).

    Примеры:
        Cache() is Cache()
        Cache().put("a", 1)
        Cache().get("a") == 1
        Cache().get("нет") is None
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def put(self, key, value):
        self._cache[key] = value

    def get(self, key):
        return self._cache.get(key)
