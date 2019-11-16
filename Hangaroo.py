# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:16:56 2019

@author: Wency
"""

def Hangaroo(secretWord):
    print('Welcome to Hangaroo!')
    print('The word Im thinking about is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('---------------------------------------')
            print('CONGRATULATIONS, YOU GUESSED IT RIGHT!')
            break
        else:
        	print('---------------------------------------')
        	print('You have', 8 - mistakesMade, 'guesses left. Think carefully!')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Good job! :', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Sorry, try again! :", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('----------------------------------------')
        	print('Sorry, you ran out of guesses. The word was', secretWord)
        	break
        else:
        	continue