# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:30:31 2019

@author: Wency
"""

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True