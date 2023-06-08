#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    l_av = len(argv) - 1

    if l_av == 3:
        operator = argv[2]
        int_a = int(argv[1])
        int_b = int(argv[3])
        if operator == "+":
            result = add(int_a, int_b)
            print("{:d} + {:d} = {:d}".format(int_a, int_b, result))
            exit(0)
        elif operator == "-":
            result = sub(int_a, int_b)
            print("{:d} - {:d} = {:d}".format(int_a, int_b, result))
            exit(0)
        elif operator == "*":
            result = mul(int_a, int_b)
            print("{:d} * {:d} = {:d}".format(int_a, int_b, result))
            exit(0)
        elif operator == "/":
            result = div(int_a, int_b)
            print("{:d} / {:d} = {:d}".format(int_a, int_b, result))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
