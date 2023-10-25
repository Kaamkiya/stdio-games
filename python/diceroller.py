import random

print('How many dice would you like to roll?')
amount_of_dice = int(input('number> '))

print('How many sides should each die have?')
amount_of_sides = int(input('number> '))

total = 0

for i in range(amount_of_dice):
	total += random.randint(1, amount_of_sides)

print('Total: %s' %total)
