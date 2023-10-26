"""
Anagrams
by Kaamkiya
"""

with open('words.txt') as f:
    words = f.readlines() # add all of the words from words.txt to a list
    
    for i, word in enumerate(words):
        words[i] = word.strip() # remove the pesky '\n' at the end of each word

def is_anagram(word1, word2):
    word1 = word1.lower() # make the words lowercase so that casing doesn't matter
    word2 = word2.lower()
    
    word1 = sorted(list(word1)) # split the words into a list and sort the letters
    word2 = sorted(list(word2)) # this permits you to compare the sotred lists
    return word1 == word2 # instead of finding another long way to do it

print('Anagrams')

print("Enter a word to see if it's an anagram")
word = input('> ').strip() # ask the user for a word

anagrams = []

for i, val in enumerate(words):
    if is_anagram(word, val):
        anagrams.append(val) # add any anagrams to the list

print('The word you entered is an anagram of')
print('\n'.join(anagrams))