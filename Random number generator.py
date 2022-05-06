import random
import sys
import time

print('Loading...')
time.sleep(1)
print('''
        Random number generator''')
time.sleep(1)
print('''             Author:BRamil
''')  # https://github.com/RBRamil
time.sleep(1)

i = 0
while i < 10:
    number1 = input('See the first number:')
    time.sleep(0.1)
    number2 = input('See the second number:')
    if not number1.isnumeric() or not number2.isnumeric():
        print('''   Error 
Please enter only an integer''')
        time.sleep(1)
        Button = input('''
N - New game
E - Exit''')
        if Button.upper() == 'N':
            print('Wait...')
            time.sleep(1)
        if Button.upper() == 'E':
            print('Wait...')
            time.sleep(1)
            sys.exit()
    else:
        number1 = int(number1)
        number2 = int(number2)
        time.sleep(1)
        print('''
And vibes %s out of %s-%s''' % (random.randint(number1, number2), number1, number2))
        time.sleep(1)
        Button = input('''
N - New game
E - Exit''')
        if Button.upper() == 'N':
            print('Wait...')
            time.sleep(1)
        if Button.upper() == 'E':
            print('Wait...')
            time.sleep(1)
            sys.exit()
