from person import Person
from worker import Worker
import sys


class Shamim(Person, Worker):

    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        Worker.__init__(self, occupation)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def detail(self):
        print(self.__str__())


person = Shamim("Shamim Sarker", 25, "Jr. Software Engineer")
person.detail()
person = Shamim("Ahmed", 29, "Associate Software Engineer")
person.detail()
person.detail_as_dict()
print(person.worker_detail())
Shamim.test_static_method()

print('Hello')
print(f"Version: {sys.version}")

num: int = 5
print(num)
