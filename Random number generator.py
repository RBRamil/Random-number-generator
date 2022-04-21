import random
import sys

print('Author: BRamil')  # https://github.com/RBRamil

i = 0
while i < 10:
    number1 = input('See the first number:')
    number2 = input('See the second number:')
    if not number1.isnumeric() or not number2.isnumeric():
        print('''Error 
    Please enter only an integer''')
        sys.exit()
    number1 = int(number1)
    number2 = int(number2)
    print('And vibes %s out of %s-%s' % (random.randint(number1, number2), number1, number2))
