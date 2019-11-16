# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:31:23 2019

@author: Wency
"""

def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return '  '.join(result)