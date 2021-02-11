import random
import datetime

def roll_dice(amount : int = 2) -> int:
    if not amount: amount = 1
    if not isinstance(amount, int): 
        amount = int(amount)
        amount = 2
    random.seed(datetime.datetime.now())
    res : str = ""
    for i in range(0, amount):
        res = res + " " + str(random.randrange(1, 7))
    return res

