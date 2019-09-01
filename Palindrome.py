# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:30:21 2019

@author: Arjan
"""

class Palindrome: 
    
    def __init__(self, potential):
        self.potential = potential
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    def checkIfPalindrome(self):
        firstPass = 0
        for i in self.alphabet:
            count = 0
            for j in self.potential:
                if i == j:
                    count = count + 1
            if count % 2 != 0:
                firstPass = firstPass + 1
            if firstPass > 1:
                return False
            
        return True
    
newPal = Palindrome("taco cat")
print(newPal.checkIfPalindrome())  