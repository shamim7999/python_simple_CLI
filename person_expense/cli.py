from argparse import ArgumentParser, Namespace
import services.cli_service as cli_serv
import services.account_service as acc_serv

parser = ArgumentParser(description='Manage your salary.')
subparsers = parser.add_subparsers(dest='command')

# Add person command
parser_add_person = subparsers.add_parser('add_person', help='Add a new person')
parser_add_person.add_argument('id', type=int, help='Person ID')
parser_add_person.add_argument('name', type=str, help='Person name')

#  Make Transaction Command
parser_make_transaction = subparsers.add_parser('make_transaction', help='Add money to a person\'s salary')
parser_make_transaction.add_argument('id', type=int, help='Account ID')
parser_make_transaction.add_argument('amount', type=float, help='Amount to add')
parser_make_transaction.add_argument('type', type=str, help='Enter Type of Transaction(Debit or Credit)')
parser_make_transaction.add_argument('date', type=str, help='Enter Date')
parser_make_transaction.add_argument('reason', type=str, help='Enter Reason to add money')
parser_make_transaction.add_argument('person_id', type=int, help="Enter person's ID")


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

# List all Persons
parser_list_persons = subparsers.add_parser('get_all_persons', help='Get List of All Persons.')

# List all Transactions
parser_list_transactions = subparsers.add_parser('get_all_transactions', help='Get List of All Transactions.')

# Salary of yy:mm
parser_salary_yy_mm = subparsers.add_parser('get_salary_by_yy_mm', help='Get Salary of a specific year and month.')
parser_salary_yy_mm.add_argument('person_id', type=int, help='Enter person id')
parser_salary_yy_mm.add_argument('year', type=str, help='Enter Year')
parser_salary_yy_mm.add_argument('month', type=str, help='Enter month')

args: Namespace = parser.parse_args()

cli_serv.setup_database()

if args.command == 'add_person':
    cli_serv.add_person(args.id, args.name)
elif args.command == 'make_transaction':
    acc_serv.make_transaction(args.id, args.amount, args.type, args.date, args.reason, args.person_id)
elif args.command == 'withdraw_money':
    cli_serv.withdraw_money(args.id, args.amount)
elif args.command == 'get_person_info':
    cli_serv.get_person_info(args.id)
elif args.command == 'delete_person':
    cli_serv.delete_person(args.id)
elif args.command == 'get_all_persons':
    cli_serv.get_all_persons()
elif args.command == 'get_salary_by_yy_mm':
    acc_serv.get_debit_for_year_month(args.year, args.month, args.person_id)
elif args.command == 'get_all_transactions':
    acc_serv.get_all_transactions()
else:
    parser.print_help()
