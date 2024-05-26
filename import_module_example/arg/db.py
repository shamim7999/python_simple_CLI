import sqlite3
import models.person as person


# Define the Person class

# Set up SQLite database
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
    cursor.execute('UPDATE person SET salary = ? WHERE id = ?', (new_salary, person_id))
    conn.commit()
    conn.close()


# Delete a person from the database
def delete_person(person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM person WHERE id = ?', (person_id,))
    conn.commit()
    conn.close()




#setup_database()

# person1 = Person(1, "John Doe", 50000.0)
# add_person(person1)
#
# retrieved_person = get_person(1)
# print(f"Retrieved: {retrieved_person}")
#
# update_person_salary(1, 55000.0)
# updated_person = get_person(1)
# print(f"Updated: {updated_person}")
#
# # Delete person from the database
# delete_person(1)
# deleted_person = get_person(1)
# print(f"Deleted: {deleted_person}")  # Should print None
