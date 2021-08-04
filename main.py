import random

from hangman_art import stages
from hangman_words import word_list
from os import system,name
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def checkGuess(char, wordList, word):
    guess = False
    for i in range(0, len(word)):
        if(word[i] == char):
            wordList[i] = char
            guess = True
    return (wordList, guess)



word = random.choice(word_list)
wordList = list('_'*len(word))
lost = False
stageVal = len(stages)-1
from hangman_art import logo

print(logo)
print(f'Pst the Word is {word}')

while('_' in wordList):
    print(' '.join([str(elem) for elem in wordList]))
    print(stages[stageVal])

    char = input("Guess a letter")
    clear()
    if char in wordList:
        print(f"you already guessed {char} correctly, try again!")
        continue
    wordList, guess = checkGuess(char, wordList, word)
    if(guess == False):
        print(f"You guessed {char} , That's not in the word, You lose a life")
        stageVal-=1
    if(stageVal<=0):
        print("You Lose!")
        lost = True
        break
print(stages[stageVal])
if not lost:
    print("You Won!")
print(word)
