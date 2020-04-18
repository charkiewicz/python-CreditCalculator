import math


def calculate_count_of_periods():
    global periods_count
    periods_count = math.ceil(math.log(
        (monthly_payment / (monthly_payment - nominal_interest_rate * principal)),
        1 + nominal_interest_rate
    ))


def calculate_monthly_payment():
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


action = input("What do you want to calculate?\n" +
               'type "n" - for count of months,\n' +
               'type "a" - for annuity monthly payment,\n' +
               'type "p" - for credit principal:')

if action != 'p':
    principal = principal = float(input("Enter credit principal"))
if action != 'a':
    monthly_payment = float(input("Enter monthly payment:"))
if action != 'n':
    periods_count = int(input("Enter count of periods:"))
interest = float(input("Enter credit interest:"))
nominal_interest_rate = interest / (12 * 100)

if action == 'a':
    calculate_monthly_payment()
    display_monthly_payment()
elif action == 'n':
    calculate_count_of_periods()
    display_count_of_periods()
else:
    calculate_credit_principal()
    display_credit_principal()
