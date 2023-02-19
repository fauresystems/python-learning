from decimal import Decimal


print('-- Precision')
x = 1 / 3
print(type(x))
print(x)
print('-----------------------')
y = Decimal(1) / Decimal(3)
print(type(y))
print(y)
print()

print('-- Calculation')
x = 0.1 + 0.1 + 0.1
print('with x = 0.1 + 0.1 + 0.1:')
print('  x == 0.3 is', x == 0.3)
print('  x =', x)
print('----------------------')
x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print("with x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1'):")
print("  x == Decimal('0.3') is", x == Decimal('0.3'))
print("  float(x) == 0.3 is", float(x) == 0.3)
print("  x =", x)
