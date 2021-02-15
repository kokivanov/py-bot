import random
import datetime

def roll_dice(args : []) -> int:

    amount = 2
    cup = 6
    if len(args) < 1:
        args.append(amount)
        args.append(cup)
    elif len(args) < 2:
        if args[0].isdigit():
            amount = int(args[0])
    elif len(args) < 3:
        if args[0].isdigit():
            amount = int(args[0])
        if args[1].isdigit():
            cup = int(args[1])

    random.seed(datetime.datetime.now())
    res: str = ""
    tmp = []

    for i in range(0, amount):
        tmp.append(random.randrange(1, cup+1))

    for i in tmp:
        res = res + str(i) + "  "

    if amount > 4:
        _sum: int = 0
        for i in tmp:
            _sum = _sum + i
        res = res + " - Sum is " + str(_sum)
    return res

def random_rn(args : []) -> int:

    a = 0
    b = 10
    if len(args) < 1:
        args.append(a)
        args.append(b)
    elif len(args) < 2:
        if not args[0].isdigit():
            args[0] = a
            args.append(b)
    elif len(args) < 3:
        if not args[0].isdigit():
            args[0] = a
        if not args[1].isdigit():
            args[1] = b

    if a > b:
        a = a + b
        b = a - b
        a = a - b

    return random.randrange(a, b+1)