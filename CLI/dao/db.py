import sqlite3
import models.person as person


def setup_database():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def not_found(person_id):
    return f"Not found person with ID: {person_id}"


def found(person_id):
    return f"Person with ID: {person_id} is already in database."


def get_person(person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, name, salary FROM person WHERE id = ?', (person_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return person.Person(*row)
    else:
        return None


def get_persons():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, salary FROM person')
    rows = cursor.fetchall()
    conn.close()
    return [person.Person(*row) for row in rows]


def add_person(person_id, person_name, person_salary):
    if get_person(person_id) is not None:
        print(found(person_id))
        return

    new_person = person.Person(person_id, person_name, person_salary)
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO person (id, name, salary) VALUES (?, ?, ?)',
                   (new_person.id, new_person.name, new_person.salary))
    print(f'Added person: {new_person}')
    conn.commit()
    conn.close()


def update_person_salary(person_id, new_salary):
    if get_person(person_id) is None:
        print(not_found(person_id))
        return

    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    person_salary = get_person_salary(person_id)

    if new_salary < 0:
        if person_salary + new_salary >= 0:
            person_salary += new_salary
            print(f"Person id: {person_id} withdrew {new_salary}")
        else:
            print("Insufficient Balance to Withdraw.")
    else:
        print(f'Added {new_salary} to person with ID {person_id}')
        person_salary += new_salary

    cursor.execute('UPDATE person SET salary = ? WHERE id = ?',
                   (person_salary, person_id))

    conn.commit()
    conn.close()


def get_person_salary(person_id):
    if get_person(person_id) is None:
        print(not_found(person_id))
        return

    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('SELECT salary FROM person WHERE id = ?', (person_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    else:
        return None


def delete_person(person_id):
    if get_person(person_id) is None:
        print(not_found(person_id))
        return
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM person WHERE id = ?', (person_id,))
    print(f'Deleted person with ID {person_id}')
    conn.commit()
    conn.close()
