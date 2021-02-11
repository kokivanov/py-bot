import random
import datetime


def roll_dice(amount: int = 2, cup: int = 6) -> int:
    if not amount:
        amount = 1

    if not isinstance(amount, int):
        amount = 2
        amount = int(amount)
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


def random_rn(a: int = 0, b: int = 10) -> int:

    if a > b:
        a = a + b
        b = a - b
        a = a - b

    return random.randrange(a, b+1)