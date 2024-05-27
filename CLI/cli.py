from argparse import ArgumentParser, Namespace
import services.cli_service as cli_serv

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

# List all Persons
parser_list_persons = subparsers.add_parser('get_all_persons', help='Get List of All Persons.')

args: Namespace = parser.parse_args()

cli_serv.setup_database()

if args.command == 'add_person':
    cli_serv.add_person(args.id, args.name, args.salary)
elif args.command == 'add_money':
    cli_serv.add_money(args.id, args.amount)
elif args.command == 'withdraw_money':
    cli_serv.withdraw_money(args.id, args.amount)
elif args.command == 'get_person_info':
    cli_serv.get_person_info(args.id)
elif args.command == 'delete_person':
    cli_serv.delete_person(args.id)
elif args.command == 'get_all_persons':
    cli_serv.get_all_persons()
else:
    parser.print_help()
