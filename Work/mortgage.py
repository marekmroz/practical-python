# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

month = 0

while principal > 0:
    extra_payment_range = range(extra_payment_start_month, extra_payment_end_month)
    _payment = payment + extra_payment if month in extra_payment_range else payment
    principal = principal * (1+rate/12) - _payment
    total_paid = total_paid + _payment
    month += 1

print('Total paid', round(total_paid, ndigits=2))
print('Months', month)
