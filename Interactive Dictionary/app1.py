# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 20:23:58 2018

@author: aryan
"""

import json
from difflib import get_close_matches


#loading json file to a python dictionary
data = json.load(open("data.json"))

def translate(word):
    
    word=word.lower()
    
    
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
        
        
    

    else:
        return "The word doesn't exist...!!! Please double check it."
    

word= input("Enter the word whose meaning you want to search..\n")

#print(translate(word))
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

    


    

    
