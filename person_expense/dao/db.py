import sqlite3
import models.person as person
import models.account as account


def setup_database():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS person2 (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY,
            amount REAL,
            type TEXT,
            date TEXT,
            reason TEXT,
            person_id INTEGER,
            FOREIGN KEY (person_id) REFERENCES person2(id)
        )
    ''')
    conn.commit()
    conn.close()


def get_total_debit_for_year_month(year, month, person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(amount) 
        FROM account 
        WHERE strftime('%Y', date) = ? 
        AND strftime('%m', date) = ? 
        AND type = 'debit'
        AND person_id = ?
    ''', (str(year), str(month).zfill(2), person_id))  # Zero-padding month if needed
    row = cursor.fetchone()
    conn.close()
    if row and row[0] is not None:
        return row[0]
    else:
        return 0  # No salary recorded for the given year and month


def get_total_debit_for_year(year, person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(amount) 
        FROM account 
        WHERE strftime('%Y', date) = ? 
        AND type = 'debit'
        AND person_id = ?
    ''', (str(year), person_id))  # Zero-padding month if needed
    row = cursor.fetchone()
    conn.close()
    if row and row[0] is not None:
        return row[0]
    else:
        return 0  # No salary recorded for the given year and month


def get_total_credit_for_year(year, person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(amount) 
        FROM account 
        WHERE strftime('%Y', date) = ? 
        AND type = 'credit'
        AND person_id = ?
    ''', (str(year), person_id))  # Zero-padding month if needed
    row = cursor.fetchone()
    conn.close()
    if row and row[0] is not None:
        return row[0]
    else:
        return 0  # No salary recorded for the given year and month


def get_total_credit_for_year_month(year, month, person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(amount) 
        FROM account 
        WHERE strftime('%Y', date) = ? 
        AND strftime('%m', date) = ? 
        AND type = 'credit'
        AND person_id = ?
    ''', (str(year), str(month).zfill(2), person_id))  # Zero-padding month if needed
    row = cursor.fetchone()
    conn.close()
    if row and row[0] is not None:
        return row[0]
    else:
        return 0  # No salary recorded for the given year and month


def make_new_transaction(account_id, amount, account_type, date, reason, person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    year, month, curr_amount = date[0]+date[1]+date[2]+date[3], date[5]+date[6], 0.0

    if account_type == 'debit':
        curr_amount = get_total_debit_for_year_month(account_id, year, month)
    else:
        curr_amount = get_total_credit_for_year_month(account_id, year, month)

    cursor.execute('''
            INSERT INTO account (id, amount, type, date, reason, person_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (account_id, amount + curr_amount, account_type, date, reason, person_id))
    conn.commit()
    conn.close()


def get_all_transaction_for_year_month(person_id, year, month):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
                SELECT * FROM account
            ''')
    rows = cursor.fetchall()
    conn.close()
    return [account.Account(*row) for row in rows]


def get_all_transactions():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('''
                SELECT * FROM account
            ''')
    rows = cursor.fetchall()
    conn.close()
    return [account.Account(*row) for row in rows]


def not_found(person_id):
    return f"Not found person with ID: {person_id}"


def found(person_id):
    return f"Person with ID: {person_id} is already in database."


def get_person(person_id):
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, name FROM person2 WHERE id = ?', (person_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return person.Person(*row)
    else:
        return None


def get_persons():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM person2')
    rows = cursor.fetchall()
    conn.close()
    return [person.Person(*row) for row in rows]


def add_person(person_id, person_name):
    if get_person(person_id) is not None:
        print(found(person_id))
        return

    new_person = person.Person(person_id, person_name)
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO person2 (id, name) VALUES (?, ?)',
                   (new_person.id, new_person.name))
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
