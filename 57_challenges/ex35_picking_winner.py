'''
Create a program that picks a winner for a contest or prize drawing.
Prompt for names of contestants until the user leaves the entry blank.
Then randomly select a winner.

Example Output
Enter a name: Homer
Enter a name: Bart
Enter a name: Maggie
Enter a name: Lisa
Enter a name: Moe
Enter a name:
The winner is... Maggie.
'''
import random

# user_input = None
def winner_game():
    while True:
        # print(contestent_name)  
        user_input = input("Type the name of the contestent: ")
        if user_input == "":
            if contestent_name:
                winner = random.choice(contestent_name)
                print(f"The winner is {winner}.")
            
            else:
                print("No contested name were entered.")
            
            break

        contestent_name.append(user_input)

contestent_name = []
winner_game()

# print(user_input)
