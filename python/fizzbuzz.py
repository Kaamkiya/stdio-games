"""
Classic Fizz Buzz

Print as many numbers as the user wants to.
If the number is divisible by 5, print Buzz.
If the number is divisible by 3, print Fizz.
If the number is divisible by both 3 and 5, print FizzBuzz.
"""
import sys

while True:
    print('How many digits would you like to print?')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()
    if response.isdecimal():
        MAX = int(response)
        break

for i in range(MAX):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('Fizz')
    else:
        print(i)
    