
def game_intro(is_intro):
    print("**************************************************************")
    if is_intro:
        print("Hello buddy, welcome to my number guessing game.")
    print("Developed by Orny Technologies")
    print("Copyright @OrnyTechnologies")

def calculate_users_score(rounds, trials):
    ratio = rounds / trials
    res = ratio * 100
    return res

def find_grade(score):
    if score > 5 and score <= 10:
        print("You are Average")
    elif score > 10 and score <= 30:
        print("You are Good")
    elif score > 30 and score <= 50:
        print("You are really very Good")
    elif score > 50 and score <= 100:
        print("You should go be a programmer")
    else:
        print("Something went wrong, could not determine your grade.")