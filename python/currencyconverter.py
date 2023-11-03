"""
A currency converter program using the frankfurter api
"""

import sys
import http
import requests

while True: # main loop
    print('What currency would you like to convert from?')
    # get an input, convert it to upper case, and remove whitespace
    from_curr = input('> ').upper().strip()

    print('What currency would you like to convert to?')
    # get the currency to convert to, convert it to uppercase, and get rid of extra whitespace
    to_curr = input('> ').upper().strip()

    try:
        print('How much money would you like to convert?')
        amount = float(input('> ')) # ask the user for an amount of money
    except ValueError: # if it's not a number, restart
        print('Not a valid number. Try again.')
        continue

    try:
        response = requests.get(
            # fetch the amount from the api
            f'https://api.frankfurter.app/latest?from={from_curr}&to={to_curr}&amount={amount}', 
            timeout=7.0 # wait a maximum of 7 seconds before giving an error or continuing
        )
    except requests.exceptions.Timeout: # if there's a timeout error
        print('The request failed with status code')
        print(http.HTTPStatus.REQUEST_TIMEOUT, 408) # give an HTTP timeout status code
        continue

    try:
        response.json()['rates']
    except KeyError:
        print('The request failed with status code')
        print(http.HTTPStatus.NOT_FOUND, 404)
        continue


    response = response.json()
    print('The amount in', to_curr, 'is ', response['rates'][to_curr], '.')

    while True:
        print('Would you like to go again? (y/n)')
        again = input('> ').lower()

        if again.startswith('y'):
            break # break out of the inner while loop, returning to main loop
        if again.startswith('n'):
            print('Thanks for using this!')
            sys.exit()
        print('Invalid response.')
