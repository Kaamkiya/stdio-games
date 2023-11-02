import time
import random

with open('../assets/sentences.txt') as f:
    SENTENCES = f.readlines()

    for i, sentence in enumerate(SENTENCES):
        SENTENCES[i] = sentence.strip()


print('''Typing speed tester

This is a game in which I give you a sentence, and you
type it as fast as you can.
''')

time.sleep(2)

while True:
    accuracy = 0
    words_per_minute = 0

    sentence = random.choice(SENTENCES) # pick a random sentence
    print('Ready...')
    time.sleep(random.randint(500, 900) / 1000) # wait a random number between 0.5 and 0.9 seconds
    print(sentence)

    start_time = time.time()
    entered = input('GO!\n').strip()
    time_taken = time.time() - start_time

    for i, char in enumerate(sentence):
        try:
            if char == entered[i]:
                accuracy += 1
        except IndexError:
            continue

    accuracy = accuracy / len(sentence) * 100 # to find the percentage
    words_per_minute = len(sentence.split(' ')) / (time_taken / 60)

    accuracy = round(accuracy, 2)
    words_per_minute = round(words_per_minute, 2)

    print('Your accuracy was', accuracy)
    print('Your words per minute (WPM) was', words_per_minute)

    print('Would you like to go again? (Y/N)')
    again = input('> ').lower()
    if again.startswith('n'):
        print('Thanks for playing!')
        break