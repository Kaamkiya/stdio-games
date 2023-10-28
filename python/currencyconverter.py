"""
A currency converter program using the frankfurter api
"""

import sys
import http
import requests

while True: # main loop
    print('What currency would you like to convert from?')
    # get an input, convert it to upper case, and remove whitespace
    from_currency = input('> ').upper().strip()

    print('What currency would you like to convert to?')
    # get the currency to convert to, convert it to uppercase, and get rid of extra whitespace
    to_currency = input('> ').upper().strip()

    try:
        print('How much money would you like to convert?')
        amount = float(input('> ')) # ask the user for an amount of money
    except ValueError: # if it's not a number, restart
        print('Not a valid number. Try again.')
        continue

    try:
        response = requests.get(
            'https://api.frankfurter.app/latest?from=%s&to=%s&amount=%s'
            %(from_currency, to_currency, amount), # fetch the amount from the api
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
    print('The amount in', to_currency, 'is ', response['rates'][to_currency], '.')

    while True:
        print('Would you like to go again? (y/n)')
        again = input('> ').lower()

        if again.startswith('y'):
            break # break out of the inner while loop, returning to main loop
        if again.startswith('n'):
            print('Thanks for using this!')
            sys.exit()
        print('Invalid response.')
