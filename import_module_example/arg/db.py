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


# Add a person to the database
def add_person(new_person):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO person (id, name, salary) VALUES (?, ?, ?)',
                   (new_person.id, new_person.name, new_person.salary))
    conn.commit()
    conn.close()


# Get a person from the database
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


# Update a person's salary in the database
def update_person_salary(person_id, new_salary):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE person SET salary = ? WHERE id = ?', (get_person_salary(person_id) + new_salary, person_id))
    conn.commit()
    conn.close()


def get_person_salary(person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('SELECT salary FROM person WHERE id = ?', (person_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]  # return the salary
    else:
        return None  # return None if the person is not found



# Delete a person from the database
def delete_person(person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM person WHERE id = ?', (person_id,))
    conn.commit()
    conn.close()
