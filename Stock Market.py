from random import gauss, randint
from time import sleep
from os import system
from matplotlib import pyplot
from threading import Thread
from datetime import date
from datetime import timedelta

stock = randint(-10, 100)
prevStock = None
highest = None
lowest = None
rate = 1.0
debtsLimit = 10
debtLimit = 5000
debtClearance = 60
debtAllowance = -10
Date = date(2007, 2, 3)

print(f"Starting with {stock}")

debts = []
for debt in debts:
    print(f"Starting with a debt of {debt}")
    stock += debt

print()
sleep(2)
system("cls")

def totalDebt() -> int:
    global debts
    if debts:
        total = 0
        for debt in debts:
            total += debt
        return total
    return 0

while True:
    print(Date)
    print()
    prevStock = stock
    stock = gauss(stock, rate)

    if not highest:
        highest = stock
    if not lowest:
        lowest = stock

    if stock > highest:
        highest = stock
    elif stock < lowest:
        lowest = stock

    print(f"Current Stock Value        : {stock} (Highest: {highest-stock}, Lowest: {lowest-stock})")
    print(f"Current Highest Stock Value: {highest}")
    print(f"Current Lowest Stock Value : {lowest}")
    if stock > prevStock:
        print(f"Stock Value increased from {prevStock} to {stock} ({stock-prevStock})")
    elif stock < prevStock:
        print(f"Stock Value decreased from {prevStock} to {stock} ({stock-prevStock})")
    else:
        print(f"Stock Value stayed the same")

    rate += gauss(round(stock-prevStock), rate)
    if rate < 0:
        rate = 1
    elif rate > 1000:
        rate = 1000

    if stock < -10:
        print()
        for _ in range(randint(1, debtsLimit)):
            if stock < debtAllowance and len(debts) < debtsLimit and totalDebt() < debtLimit:
                debt = min(debtLimit-totalDebt(), randint(10, 50)-stock)
                if debt:
                    print(f"Borrowing a Debt of {debt}")
                    stock += debt
                    print(f"Stock Value Increased from {stock-debt} to {stock}")
                    debts.append(debt)
            else:
                pass

    cs = []
    for debt in debts:
        if stock > debt and stock > debtClearance:
            stock -= debt
            cs.append(debt)
            debts.remove(debt)
    if cs:
        print()
        for c in cs:
            print(f"A Debt of {c} has been cleared")

    if debts:
        print()
        print("Debts:")
        debts.sort()
        for _ in range(debts.count(0)):
            debts.remove(0)
        for debt in debts:
            print(f"    {debt}")
        if len(debts) > 1:
            print()
            print(f"    {totalDebt()}")

    Date += timedelta(1)

    sleep(1)
    system("cls")

def update():
    pass

def visualize():
    pass

def write():
    pass