"""Guess a Number Game
Computer plays agains itself"""

import numpy as np # NumPy contains random module that we'll need for the game

def random_predict(number: int=1) -> int:
    """ Using random to guess a number

    Args:
        number (int, optional): Number to guess. Defaults to 1.

    Returns:
        int: Number of tries
    """
    
    count = 0 # Number of tries
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Computer makes a guess
        if number == predict_number:
            break # Cycle ends when the guess is correct    
    return(count)    

# print(f"Number of tries: {random_predict(10)}") 

# Adding a modification that'll allow us to get the average number of tries 
# computer needs to guess the right number using our algorithm
def score_game(random_predict) -> int:
    """ Function calculates the average number of tries computer needs to make the right guess (based on 1000 takes)

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Average number of tries
    """
    count_ls = [] # Number of tries
    np.random.seed(1) # Method seed() initiates the start number and saves the state of function,
    # so it can generate same random numbers on multiple execution. Responsible for reproducibility.
    random_array = np.random.randint(1, 101, size=(1000)) # Creating a list of 1000 numbers to calculate the average number of tries
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Your algorithm helps the computer to guess the correct number in the average of {score} tries.")
    return(score)

if __name__ == "__main__": # Special command that stops print() 
# unless the file is imported as function and not a library   
    score_game(random_predict) # RUN