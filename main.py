import random
from scores.utils import game_intro, find_grade, calculate_users_score


game_intro(is_intro=True)

round_trials = []
number_of_plays = 0
while True:
    # ask the user if they wish to play the game
    question = input("'p' to play and 'q' to quit: ")
    if question == 'p': # the user wants to play another round
        number_of_plays += 1
        secret_number = random.randint(1, 100) # creates a random number between 1 and 100
        print(secret_number)
        trials = 0
        guess = 0
        while (secret_number != guess):
            try:         
                guess = int(input("enter guess: "))
            except ValueError:
                # continue
                print("Invalid input, can only accept integers")
                continue
            except:
                print("Something went wrong")
                continue
            trials = trials + 1  
            if guess == secret_number:
                print(f"you guessed the number {secret_number} in {trials} amount of trials")
                round_trials.append(trials) # add the trials to list of trials
                break
            elif guess > secret_number:
                print("above secret number")
            else:
                print("below secret number")
    
    elif question == 'q':
        if len(round_trials) > 0:
            # the user wants to quit the game
            # Show the user how many trials there did in each round
            enum_rounds_trials = enumerate(round_trials) # create an enum datastructure to store both data and indexes
            for index, value in enum_rounds_trials:
                print(f"You Round {index+1} of Play was: {value}")
            print(f"you played {number_of_plays} rounds")   
            # give the user the final score 
            sum_of_trials = sum(round_trials) # sum all the trials in the list
            score = calculate_users_score(number_of_plays, sum_of_trials)
            find_grade(score)
            print(f"Your score is: {score}")
        
        print("Quiting the game, bye.")
        break


game_intro(is_intro=False)
