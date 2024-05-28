class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def __str__(self):
        return f"Person(id={self.id}, name='{self.name})'"
