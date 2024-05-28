import random
def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors:)")
    options = ["rock", "paper", "scissors"]
    compter_choice = random.choice(options)
    choices = {"player": player_choice, "computer": compter_choice}
    return choices

def check_win(player, computer):
    print(f"You Chose {player} Compter chose {computer}")
    if player == computer:
     return"It's tie! "
    elif player == "rock": 
        if computer == "scissors":
            return "Rock Smashes Sciccors! You Win!"
        else:
            return "Paper covers Rock! You Lose."
        
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers Rock ! You Win!"
        else:
            return "Scissors cuts Paper ! You Lose."  

    elif player == "scissors": 
        if computer == "paper":
            return "Sciccors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You Lose."      
      
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
    
    





