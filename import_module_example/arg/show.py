from collections import defaultdict

my_salary = defaultdict(lambda: defaultdict(float))


def print_money_by_year(year):
    print(f'Money for the year {year}:')
    for month, money in my_salary[year].items():
        print(f'{month}: {money}')
    if not my_salary[year]:
        print("Nothing Available")


while True:
    print("Enter Year: ", end='')
    y = int(input())
    print_money_by_year(y)
