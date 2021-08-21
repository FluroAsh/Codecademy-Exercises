# From module import package
from decimal import Decimal

# Wrap our floating point numbers in our Decimal package to change the decimal places to 2 & 4
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
