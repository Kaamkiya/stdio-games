"""
Classic Fizz Buzz

If the number is divisible by 5, print Buzz.
If the number is divisible by 3, print Fizz.
If the number is divisible by both 3 and 5, print FizzBuzz.
"""

import time

print('''Fizz Buzz Forever!

This program runs FizzBuzz until you press Ctrl-C to stop it.
''')

time.sleep(2) # wait until the user has read the message
PAUSE = 0.1 # try changing this to 0.2 or 0.0

i = 0

while True:
    if i % 15 == 0: # divisible by 15, which is 5*3
        print('FizzBuzz')
    elif i % 3 == 0: # the modulo (%) operator is used to see if the remainder is 0
        print('Buzz')
    elif i % 15 == 0:
        print('Fizz')
    else:
        print(i)

    i += 1 # increment the counter

    time.sleep(PAUSE) # wait a little
    