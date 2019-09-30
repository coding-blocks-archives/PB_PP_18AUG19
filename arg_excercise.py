


import argparse


def calculator(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--x', type=float,default=1.0,
            help='What is the first number.')
    parser.add_argument('-y', '--y', type=float,default=1.0,
            help='What is the second number.')
    parser.add_argument('-op', '--operation', type=str, default='add',
            help='What operation? You can choose from add, sub, mul or div. ')
    args = parser.parse_args()
    print(calculator(args))

if __name__ == '__main__':
    main()
