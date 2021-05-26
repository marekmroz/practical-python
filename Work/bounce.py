# bounce.py
#
# Exercise 1.5

"""
A rubber ball is dropped from a height of 100 meters and each time it hits the
ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py
 that prints a table showing the height of the first 10 bounces.
"""

height = 100.0
bounce_factor = 0.6
bounce_count = 10

for i in range(bounce_count):
    height *= bounce_factor
    print(i + 1, round(height, ndigits=4))
