"""
Reflexes

A test to see how fast the user reacts on seeing the word DRAW. 
"""

import sys
import time
import random

def main():
    """Main program. Everything happens here, and the while True calls this."""
    print("You're walking along a beach...")
    time.sleep(random.randint(1000, 4000) / 1000)

    draw_time = time.time()
    print('DRAW!')
    input()
    time_elapsed = time.time() - draw_time

    if time_elapsed < 0.01:
        print('You pressed enter before the word draw! You lose!')
    elif time_elapsed > 0.5:
        time_elapsed = round(time_elapsed, 4)
        print('You took too long:', time_elapsed, 'seconds.')
    else:
        time_elapsed = round(time_elapsed, 4)
        print('You were fast! It took you ', time_elapsed,' seconds to react.')

print('Welcome to reflexes!')
print('When you see the word DRAW, press enter as fast as you can.')
print('Press ctrl-c to quit.')
print('Press enter to continue...', end='')
input()
while True:
    try:
        main()
    except KeyboardInterrupt:
        print('Thanks for playing!')
        sys.exit()
