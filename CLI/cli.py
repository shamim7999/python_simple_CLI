# main.py
from argparse import ArgumentParser, Namespace
import dao.db as mydb
import models.person as person_module


def add_money(person_id, amount):
    mydb.update_person_salary(person_id, amount)
    print(f'Added {amount} to person with ID {person_id}')


def withdraw_money(person_id, amount):
    mydb.update_person_salary(person_id, -amount)
    print(f'Withdrew {amount} from person with ID {person_id}')


def get_person_info(person_id):
    person = mydb.get_person(person_id)
    if person:
        print(f'Person Info: {person}')
    else:
        print(f'No person found with ID {person_id}')


def delete_person(person_id):
    mydb.delete_person(person_id)
    print(f'Deleted person with ID {person_id}')


def add_person(person_id, person_name, person_salary):
    new_person = person_module.Person(person_id, person_name, person_salary)
    mydb.add_person(new_person)
    print(f'Added person: {new_person}')


mydb.setup_database()


parser = ArgumentParser(description='Manage your salary.')
subparsers = parser.add_subparsers(dest='command')

# Add person command
parser_add_person = subparsers.add_parser('add_person', help='Add a new person')
parser_add_person.add_argument('id', type=int, help='Person ID')
parser_add_person.add_argument('name', type=str, help='Person name')
parser_add_person.add_argument('salary', type=float, help='Person salary')

# Add money command
parser_add_money = subparsers.add_parser('add_money', help='Add money to a person\'s salary')
parser_add_money.add_argument('id', type=int, help='Person ID')
parser_add_money.add_argument('amount', type=float, help='Amount to add')

# Withdraw money command
parser_withdraw_money = subparsers.add_parser('withdraw_money', help='Withdraw money from a person\'s salary')
parser_withdraw_money.add_argument('id', type=int, help='Person ID')
parser_withdraw_money.add_argument('amount', type=float, help='Amount to withdraw')

# Get person info command
parser_get_person = subparsers.add_parser('get_person_info', help='Get information about a person')
parser_get_person.add_argument('id', type=int, help='Person ID')

# Delete person command
parser_delete_person = subparsers.add_parser('delete_person', help='Delete a person')
parser_delete_person.add_argument('id', type=int, help='Person ID')

args: Namespace = parser.parse_args()

if args.command == 'add_person':
    add_person(args.id, args.name, args.salary)
elif args.command == 'add_money':
    add_money(args.id, args.amount)
elif args.command == 'withdraw_money':
    withdraw_money(args.id, args.amount)
elif args.command == 'get_person_info':
    get_person_info(args.id)
elif args.command == 'delete_person':
    delete_person(args.id)
else:
    parser.print_help()
