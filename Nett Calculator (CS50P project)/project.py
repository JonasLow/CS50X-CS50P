import re
import sys

def main():
    #FUNCTION 1
    participants = []
    while True:
        try:
            get_name(participants)

        except EOFError:
            print("\n")
            break

    #FUNCTION 2
    ledger = {}
    i = 0
    for i in range(len(participants)):
        ledger.update({participants[i] : 0})

    while True:
        try:
            amount = input("Transaction: ")
            correct_format = transaction_format(amount)
            if correct_format:
                pieces = correct_format.groups()
                name = pieces[0].lower()
                money = float(pieces[2])

                if name in participants:
                    if name in ledger:
                        ledger[name] = float(ledger.get(name)) + money

                    else:
                        ledger[name] = money

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("Invalid Format/Name", end="\n")
            pass

        except EOFError:
            print("\n")
            break

    pay_roll = nett(ledger)

    for name in pay_roll:
        if pay_roll[name] < 0:
            print(f"{name} owes ${-pay_roll[name]:.2f}")

        elif pay_roll[name] > 0:
            print(f"{name} receives ${pay_roll[name]:.2f}")

        else:
            print(f"{name} is Nett Zero")


def get_name(x):
    _name = input("Who is coming? ")
    x.append(_name.lower())
    return x



def transaction_format(amount):
    check = re.search(r"([a-z_A-Z]+)\,( ?\$)(\d+(\.\d+)?)", amount)
    return check


def nett(x):
    pool = sum(x.values())

    for name in x.keys():
        to_pay = float(x[name]) - (pool) / len(x)
        x.update({name: to_pay})

    return x


if __name__ == "__main__":
    main()