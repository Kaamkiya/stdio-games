import random

number = random.randint(1, 100) # random number between 1 and 100

print("I'm thinking of a number between 1 and 100")
while True:
	print('Take a guess')
	guess = int(input('> ')) # get the user's guess

	if guess == number:
		print('Correct! You win!')
		break
	elif guess > number:
		print('Your guess is too high')
	elif guess < number:
		print('Your guess is too low')
