class Person:
    def __init__(self, person_id, name, salary):
        self.id = person_id
        self.name = name
        self.salary = salary

    def add_money(self, money):
        if money < 0:
            if self.salary + money >= 0:
                self.salary += money
            else:
                print("You have insufficient Balance to withdraw.")
            return
        self.salary += money

    def __str__(self):
        return f"Person(id={self.id}, name='{self.name}', salary={self.salary})"
