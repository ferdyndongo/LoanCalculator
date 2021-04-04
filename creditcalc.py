#!/usr/bin/env python3

import argparse
import sys
import math


def check_input():

    parser = argparse.ArgumentParser()

    parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters")

    parser.add_argument("--payment")

    parser.add_argument("--principal")

    parser.add_argument("--periods")

    parser.add_argument("--interest")

    args = parser.parse_args()

    if not(args.type == "annuity" or args.type == "diff"):
        print("Incorrect parameters")
        return False
    elif args.payment and args.type == "diff":
        print("Incorrect parameters")
        return False
    elif not args.interest:
        print("Incorrect parameters")
        return False
    elif len(sys.argv) - 1 < 4:
        print("Incorrect number of parameters")
        return False
    else:
        if args.type == "diff":
            t = args.type
            i = float(args.interest) / 100 / 12
            p = int(args.principal)
            n = int(args.periods)
            return t, i, p, n
        else:
            t = args.type
            i = float(args.interest) / 100 / 12
            p = args.principal
            n = args.periods
            a = args.payment
            return t, i, p, n, a


if check_input():
    arg = check_input()
    i = arg[1]
    if arg[0] == "diff":
        p = arg[2]
        n = arg[3]
        D = []
        for m in range(1, n + 1):
            d = math.ceil((p/n) + i * (p - ((p * (m - 1)) / n)))
            print(f"Month {m}: payment is {d}")
            D.append(d)
        print(f"\nOverpayment = {sum(D) - p}")
    else:
        if arg[2] is None:
            n = int(arg[3])
            a = int(arg[4])
            p = math.floor(a / ((i * math.pow(1 + i, n))/(math.pow(1 + i, n) - 1)))
            print(f"Your loan principal = {p}!")
            print(f"Overpayment = {a * n - p}")
        elif arg[3] is None:
            p = int(arg[2])
            a = int(arg[4])
            n = math.ceil(math.log(a / (a - i * p), 1 + i))
            if n % 12 == 0:
                print(f"It will take {int(n / 12)} years to repay this loan!")
            else:
                print(f"It will take {int(n / 12)} years and {n % 12} months to repay this loan!")
            print(f"\nOverpayment = {a * n - p}")
        elif arg[4] is None:
            p = int(arg[2])
            n = int(arg[3])
            a = math.ceil(p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
            print(f"Your annuity payment = {a}!")
            print(f"\nOverpayment = {a * n - p}")
