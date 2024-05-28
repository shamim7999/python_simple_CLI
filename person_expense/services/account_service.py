import dao.db as mydb


def make_transaction(account_id, amount, transaction_type, date, reason, person_id):
    mydb.make_new_transaction(account_id, amount, transaction_type, date, reason, person_id)


def get_all_transactions():
    print(*mydb.get_all_transactions(), sep='\n')


def get_debit_for_year_month(year, month, person_id):
    print(mydb.get_debit_for_year_month(year, month, person_id))
