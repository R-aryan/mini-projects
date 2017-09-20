### --- CODEBREAKER --- ###
## --Nope--Close--Match--##
###########################

# It's time to actually make a simple command line game so put together everything
#  The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match, the game will report "CODE CRACKED"!



import random

#get guess from the user

def get_guess():
    #print("Enter your guesss ")
    return list(input("What is your guess   "))

# generate random computer code
def generate_code():

    digit= [str(num) for num in range(10)]

    #shuffle the digits using random
    random.shuffle(digit)
    # grab first 3 digit from the list
    #print(digit[:3])
    return digit[:3]


#generate the clues for the user

def generate_clues(code ,user_guess):

    if user_guess==code:
        return "CODE CRACKED"
    
    clues=[]

    for ind,num in enumerate(user_guess):

        if num==code[ind]:
            clues.append("Match")
        
        elif num in code:
            clues.append("Close")
        
    
    if clues == []:
        return ["Nope"]
    else:
        return clues





#running main game logic

print("Welcome to the code breaker Game ")

secret_code = generate_code()

clue_report = []

while clue_report!="CODE CRACKED":
    guess = get_guess()

    clue_report= generate_clues(secret_code,guess)

    print("Here is the result of your Guess")

    for clue in clue_report:
        print(clue)



