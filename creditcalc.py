import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()

if args.type != 'annuity' and args.type != 'diff':
    print('Incorrect parameters')
if args.payment is None and args.type == 'diff':
    print('Incorrect parameters')
if args.interest is None:
    print('Incorrect parameters')
    exit()
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment
tip = args.type
variable_list = [principal, periods, interest, payment, tip]

ok = 0
for i in variable_list:
    if i is None:
        ok += 1
if ok > 1:
    print('Incorrect parameters')
    exit()

interest_rate = interest / (12 * 100)

# 1
if payment is None and tip == 'diff':
    overpayment = 0
    total_payment = 0
    for m in range(1, periods + 1):
        d = principal / periods + interest_rate * (principal - (principal * (m - 1)) / periods)
        d = int(math.ceil(d))
        total_payment += d
        print(f'Month {m}: payment is {d}')
    overpayment = total_payment - principal
    print()
    print(f'Overpayment = {overpayment}')
if payment is None and tip == 'annuity':
    annuity = principal * interest_rate * pow(1 + interest_rate, periods) / (pow(1 + interest_rate, periods) - 1)
    annuity = math.ceil(annuity)
    print(f'Your annuity payment = {annuity}!')
    print(f'Overpayment = {math.ceil(annuity * periods - principal)}')
if tip == 'annuity' and principal is None:
    elem = pow(1 + interest_rate, periods)
    loan_principal = payment / (interest_rate * elem / (elem - 1))
    print(f'Your loan principal = {math.floor(loan_principal)}!')
    print(f'Overpayment = {math.ceil(payment * periods - loan_principal)}')
if tip == 'annuity' and periods is None:
    number_of_months = math.log(payment / (payment - interest_rate * principal), 1 + interest_rate)
    number_of_months = math.ceil(number_of_months)
    if number_of_months < 12:
        print(f'It will take {number_of_months} months to repay this loan!')
    elif number_of_months == 12:
        print('It will take 1 year to repay this loan!')
    else:
        years = number_of_months // 12
        months = number_of_months
        number_of_months = number_of_months % 12
        if number_of_months == 0:
            print(f'It will take {years} years to repay this loan!')
        else:
            print(f'It will take {years} years and {number_of_months} months to repay this loan!')
    print(f"Overpayment = {math.ceil(payment * months - principal)}")
