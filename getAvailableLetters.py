# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:31:38 2019

@author: Wency
"""

import string
alphabet = string.ascii_lowercase

def getAvailableLetters(lettersGuessed): 
    remain = []
    for i in alphabet:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
