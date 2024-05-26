from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    def name(self, name):
        self._name = name

    @property
    @abstractmethod
    def age(self):
        pass

    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return f"Person's (name={self._name}, age={self._age})"

    @staticmethod
    def test_static_method():
        print("This is a static method")

    def detail_as_dict(self):
        print(self.__dict__)

    @abstractmethod
    def detail(self):
        pass

