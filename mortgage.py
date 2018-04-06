# mortgage.py
import math

def mortgage_payment(loan, periods, rate):
    payment = (rate * loan)/(1 - (1 + rate)**（-periods)）
    return(mortgage_payment)

print('Calculate the period mortage payment !')
loan = float(input('Tell me the value of your loan :'))
rate = float(input('Tell me the per-period interets rate :'))
periods = float(input('Tell me the periods :'))

mortgage_payment = mortgage_payment(loan, periods, rate)
print('Hey! Your period mortgage payment is ', mortgage_payment)
