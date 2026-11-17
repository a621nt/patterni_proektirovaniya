"""Домашнее задание. Тема 3: наследование и super()."""


class PersonA:
    """Задание 08. super() в переопределённом методе.

    PersonA(name).introduce() возвращает "Меня зовут {name}".
    StudentA(name, university) переопределяет introduce(), ВЫЗЫВАЯ
    super().introduce() и дописывая ", учусь в {university}".

    Примеры:
        PersonA("Иван").introduce() == "Меня зовут Иван"
        StudentA("Иван", "МГУ").introduce() == "Меня зовут Иван, учусь в МГУ"
    """

    def __init__(self, name):
        self.name = name

    def introduce(self):
        raise NotImplementedError("Реализуйте PersonA.introduce")


class StudentA(PersonA):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def introduce(self):
        raise NotImplementedError("Реализуйте StudentA.introduce (через super())")


class BaseAccount:
    """Задание 09. Сберегательный счёт.

    BaseAccount(owner, balance): баланс — свойство balance (только
    чтение), метод deposit(amount) пополняет счёт.
    SavingsAccount(owner, balance, rate) добавляет rate (проценты в год);
    метод add_interest() увеличивает баланс на rate процентов (округление
    до двух знаков) и возвращает новый баланс.

    Примеры:
        acc = SavingsAccount("Анна", 1000, 5)
        acc.balance == 1000
        acc.add_interest() == 1050.0
        acc.balance == 1050.0
        acc.deposit(50)
        acc.balance == 1100.0
    """

    def __init__(self, owner, balance):
        raise NotImplementedError("Реализуйте BaseAccount.__init__")

    @property
    def balance(self):
        raise NotImplementedError("Реализуйте BaseAccount.balance")

    def deposit(self, amount):
        raise NotImplementedError("Реализуйте BaseAccount.deposit")


class SavingsAccount(BaseAccount):
    def __init__(self, owner, balance, rate):
        raise NotImplementedError("Реализуйте SavingsAccount.__init__")

    def add_interest(self):
        raise NotImplementedError("Реализуйте SavingsAccount.add_interest")


class QueueList(list):
    """Задание 10. Очередь на базе встроенного list.

    Наследуйте list и реализуйте очередь:
      enqueue(item) — в конец;
      dequeue()     — из начала (для пустой очереди — естественный IndexError);
      front()       — первый элемент без извлечения;
      size()        — число элементов.

    Примеры:
        q = QueueList()
        isinstance(q, list) == True
        q.enqueue("первый"); q.enqueue("второй")
        q.size() == 2
        q.front() == "первый"
        q.dequeue() == "первый"
        q.dequeue() == "второй"
        q.dequeue()  # IndexError
    """

    def enqueue(self, item):
        raise NotImplementedError("Реализуйте QueueList.enqueue")

    def dequeue(self):
        raise NotImplementedError("Реализуйте QueueList.dequeue")

    def front(self):
        raise NotImplementedError("Реализуйте QueueList.front")

    def size(self):
        raise NotImplementedError("Реализуйте QueueList.size")
