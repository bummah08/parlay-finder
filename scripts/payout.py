#!/usr/bin/env python3
"""Calculate the conditional return from one quoted whole-ticket price."""
import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, getcontext


def number(raw):
    try:
        value = Decimal(raw)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError("Enter a number.") from error
    if not value.is_finite():
        raise argparse.ArgumentTypeError("Enter a finite number.")
    return value


def fraction(raw):
    parts = raw.split("/")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("Use fractional odds such as 5/2.")
    top, bottom = map(number, parts)
    if top <= 0 or bottom <= 0:
        raise argparse.ArgumentTypeError("Both parts of fractional odds must be positive.")
    return 1 + top / bottom


def main():
    getcontext().rounding = ROUND_HALF_UP
    parser = argparse.ArgumentParser(description=__doc__)
    prices = parser.add_mutually_exclusive_group(required=True)
    prices.add_argument("--cents", type=number, help="Buy price in cents per $1 winning contract")
    prices.add_argument("--decimal", type=number, help="Decimal odds including the returned stake")
    prices.add_argument("--american", type=number, help="American odds such as +150 or -125")
    prices.add_argument("--fractional", type=fraction, help="Fractional odds such as 5/2")
    parser.add_argument("--budget", type=number, default=Decimal(10), help="Total cash budget")
    parser.add_argument("--entry-fee", type=number, default=Decimal(0), help="Known entry fee for this size")
    parser.add_argument("--win-fee", type=number, default=Decimal(0), help="Known fee deducted only on a win")
    parser.add_argument("--lot", type=number, help="Contract quantity increment for a price in cents")
    args = parser.parse_args()

    if args.budget <= 0 or not 0 <= args.entry_fee < args.budget or args.win_fee < 0:
        parser.error("Use a positive budget, an entry fee below the budget, and nonnegative fees.")
    if args.lot is not None and (args.cents is None or args.lot <= 0):
        parser.error("Use a positive --lot only with --cents.")

    stake = args.budget - args.entry_fee
    if args.cents is not None:
        if not 0 < args.cents < 100:
            parser.error("The price of an open contract must be between 0 and 100 cents, exclusive.")
        unit_cost = args.cents / 100
        if args.lot is None:
            gross = stake / unit_cost
        else:
            lots = stake // (unit_cost * args.lot)
            if lots == 0:
                parser.error("This budget cannot buy one lot at the supplied price and fee.")
            gross = lots * args.lot
            stake = gross * unit_cost
    else:
        if args.american is not None:
            if abs(args.american) < 100:
                parser.error("American odds must be at least +100 or at most -100.")
            if args.american > 0:
                odds = 1 + args.american / 100
            else:
                odds = 1 + 100 / abs(args.american)
        elif args.decimal is not None:
            if args.decimal <= 1:
                parser.error("Decimal odds must exceed 1.")
            odds = args.decimal
        else:
            odds = args.fractional
        gross = stake * odds

    spend = stake + args.entry_fee
    receipt = gross - args.win_fee
    if receipt <= 0:
        parser.error("The win fee must leave a positive winning return.")
    print("Amounts use the budget currency. Only supplied fees are included.")
    print(f"Committed from budget: {spend:.2f}")
    print(f"Budget left: {args.budget - spend:.2f}")
    print(f"Gross return if all legs win: {gross:.2f}")
    if args.win_fee:
        print(f"Winning return after supplied win fee: {receipt:.2f}")
    print(f"Profit if all legs win: {receipt - spend:.2f}")
    print(f"Loss if the ticket settles at zero: {spend:.2f}")
    print(f"Break-even win rate for binary settlement: {100 * spend / receipt:.2f}%")


if __name__ == "__main__":
    main()
