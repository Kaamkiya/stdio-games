"""Collatz Conjunction

The Collatz Conjunction is a sequence starting with the number n.

The next number is found by the following rules:
1. If n is even, the next number is n / 2
2. If n is odd, the next number is n * 3 + 1
3. If n is one, stop.
"""

import sys
import time

print('''The Collatz conjunction is a sequence of numbers starting with the number n.

The next number is found by the following rules:
1. If n is even, the next number is n / 2
2. If n is odd, the next number is n * 3 + 1
3. If n is one, stop, otherwise, repeat.
''')

print('Enter a starting number (greater than 0) or QUIT:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()

amount_of_steps = 0

n = int(response)

print(n, end='', flush=True)

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

    print(',', str(n), end='', flush=True)
    time.sleep(0.1)
    amount_of_steps += 1

print('\nAmount of steps taken to get to 1:', str(amount_of_steps))
print()
