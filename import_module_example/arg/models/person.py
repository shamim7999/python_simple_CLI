class Person:
    def __init__(self, person_id, name, salary):
        self.id = person_id
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Person(id={self.id}, name='{self.name}', salary={self.salary})"

