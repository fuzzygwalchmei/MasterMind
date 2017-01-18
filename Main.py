#Imports
import random
import Features

#Define a 4 digit number
targetNumber = random.randint(1000, 9999)

print(targetNumber)
#15 turns to guess it correctly
turns = 15
counter = 0
#Loop

print("Take your guess, 0 indicates a number in the correct spot, ? means a correct number in the wrong location, and X means the number is not in the answer\n")
while counter != turns:

    #accept input of choices
    playerGuess = int(input("Please enter your guess (between 1000 and 9999): "))

    #run function to check entry
    Features.compareValue(targetNumber,playerGuess)

    counter+=1
    #if:
    if Features.CheckValue(targetNumber,playerGuess):
        print("You guessed it!")
        break
        #correct - Congratulate and end
    #else:
else:
    # wrong - display correct position (0), wrong Position (?) and wrong (X)
    print("Sorry, Try again!")


#end