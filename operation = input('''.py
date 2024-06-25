operation = input('''
Please type in the math operation you would like to complete:
ADD for +
SUB for -
MUL for *
DIV for /
MOD for %
POW for **
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)

print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)

print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)

print('{} % {} = '.format(number_1, number_2))
print(number_1 / number_2)

print('{} ** {} = '.format(number_1, number_2))
print(number_1 / number_2)