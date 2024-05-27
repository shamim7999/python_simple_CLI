import dao.db as mydb


def add_money(person_id, amount):
    mydb.update_person_salary(person_id, amount)


def withdraw_money(person_id, amount):
    mydb.update_person_salary(person_id, -amount)


def get_all_persons():
    print(*mydb.get_persons(), sep='\n')


def get_person_info(person_id):
    person = mydb.get_person(person_id)
    if person:
        print(f'Person Info: {person}')
    else:
        print(f'No person found with ID {person_id}')


def delete_person(person_id):
    mydb.delete_person(person_id)


def add_person(person_id, person_name, person_salary):
    mydb.add_person(person_id, person_name, person_salary)


def setup_database():
    mydb.setup_database()