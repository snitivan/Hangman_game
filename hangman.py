# Write your code here
"""import random

print("H A N G M A N")
list_of_words = ['python', 'java', 'kotlin', 'javascript']
rand_word = random.choice(list_of_words)
hint = rand_word[:3] + '-' * (len(rand_word) - 3)
word = input(f'Guess the word: {hint}: > ')


if word == rand_word:
    print('You survived!')
else:
    print('You are hanged!')"""

import random


def hint_word(r_word):
    lst = []
    for i in enumerate(r_word):
        lst.append(i)
    lst1 = []
    for let in range(len(lst)):
        lst1.append(lst[let][1].replace(lst[let][1], '-'))
    n = 0
    inp_set = set()
    while n != 8:
        print('\n')
        print(*lst1, sep='')
        letter = input(f'Input a letter: > ')
        word_set = set(r_word)
        if letter in inp_set and len(letter) < 2:
            print('You already typed this letter')
        elif len(letter) > 1:
            print('You should input a single letter')
        elif not letter.isalpha() or not letter.islower():
            print('It is not an ASCII lowercase letter')
        else:
            if letter in word_set:
                if letter in lst1:
                    print('You already typed this letter')
                elif len(letter) > 1:
                    print('You should input a single letter')
                elif letter.isalpha() and not letter.islower():
                    print('It is not an ASCII lowercase letter')
                else:
                    x = 0
                    while x != -1:
                        ind = r_word.find(letter, x, len(r_word))
                        if ind == -1:
                            x = -1
                        else:
                            x = ind + 1
                            lst1[ind] = letter
            else:
                print('No such letter in the word')
                n += 1
            if word_set == set(lst1):
                print(f'You guessed the word{r_word}!\nYou survived!')
                break
        inp_set.add(letter)
    else:
        print("You are hanged!\n")


print("H A N G M A N")
while True:
    start = input('Type "play" to play the game, "exit" to quit: > ')
    if start == 'play':
        list_of_words = ['python', 'java', 'kotlin', 'javascript']
        rand_word = random.choice(list_of_words)
        hint_word(rand_word)
    elif start == 'exit':
        break
    else:
        print('Please write only play or exit')
