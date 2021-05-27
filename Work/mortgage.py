# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 0

while principal > 0:
    _payment = payment + 1000.0 if month < 12 else payment
    principal = principal * (1+rate/12) - _payment
    total_paid = total_paid + _payment
    month += 1

print('Total paid', round(total_paid, ndigits=2), 'Months', month)
