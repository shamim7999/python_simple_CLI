import argparse


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple CLI for arithmetic operations")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("x", type=float, help="First operand")
    parser.add_argument("y", type=float, help="Second operand")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.x, args.y)
    elif args.operation == "subtract":
        result = subtract(args.x, args.y)
    elif args.operation == "multiply":
        result = multiply(args.x, args.y)
    elif args.operation == "divide":
        result = divide(args.x, args.y)

    print(f"Result of {args.operation} {args.x} and {args.y} is: {result}")
