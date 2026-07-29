'''
Create a Magic 8 Ball game that prompts for a question and then displays either “Yes,” “No,” “Maybe,” or “Ask again later.”

Example Output
What's your question? Will I be rich and famous?
Ask again later.
'''
import random

def magic_game(random_ans, user_que):
    #this will randomly choice the answer from the list provided.
    out_ans = random.choice(random_ans)
    print(out_ans)

random_ans = ["Yes", "No", "Maybe", "Ask again later."]
user_que = input("What's your question? ")

magic_game(random_ans, user_que)



