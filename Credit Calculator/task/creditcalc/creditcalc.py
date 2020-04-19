import math
import argparse


def calculate_periods_annuity():
    global periods_count
    periods_count = math.ceil(math.log(
        (monthly_payment / (monthly_payment - nominal_interest_rate * principal)),
        1 + nominal_interest_rate
    ))


def calculate_annuity_payment():
    global monthly_payment
    monthly_payment = math.ceil(principal * nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods_count)
                                / (math.pow(1 + nominal_interest_rate, periods_count) - 1))


def calculate_credit_principal():
    global principal
    principal = monthly_payment / (
            (nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods_count)) /
            (math.pow(1 + nominal_interest_rate, periods_count) - 1)
    )


def display_count_of_periods():
    years = periods_count // 12
    months = periods_count - 12 * years
    msg = 'You need '
    if years != 0:
        msg += '{0} years and '.format(years)
    if months != 0:
        msg += '{0} months'.format(months)
    msg += ' to repay this credit!'
    print(msg)


def display_monthly_payment():
    print("Your annuity payment = {0}".format(monthly_payment))


def display_credit_principal():
    print("Your credit principal = {0}".format(math.floor(principal)))


def diff_payment():
    return


def annuity_payment():
    return


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of payment")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
if args.type != 'diff' or args.type != 'annuity':
    print("Incorrect parameters")
elif args.type == 'diff' and (args.periods is None or args.principal is None):
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == 'diff':
    diff_payment()
else:
    annuity_payment()


#principal
#monthly_payment
#periods_count
#interest
#nominal_interest_rate = interest / (12 * 100)
