"""Guess a Number Game"""

import numpy as np

number = np.random.randint(1, 101) # Setting a randome number

# Creating game's logic
count = 0 # Количество попыток

while True:
    count += 1
    predict_number = int(input("Guess a number from 1 to 100"))
    
    if predict_number > number:
        print("The number should be smaller!")
        
    elif predict_number < number:
        print("The number should be bigger!")
        
    else:
        print(f"You've guessed it right! The number is {number}. Number of tries: {count}.")
        break # The guess is correct. End of cycle