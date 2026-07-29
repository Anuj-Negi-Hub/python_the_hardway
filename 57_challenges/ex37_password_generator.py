'''
Create a program that generates a secure password.
Prompt the user for the minimum length, the number of special characters, and the number of numbers.
Then generate a password for the user using those inputs.

Example Output
What's the minimum length? 8
How many special characters? 2
How many numbers? 2
Your password is aurn2$1s#
'''
import random

def password_generator(letters, num_list, special_char):

    min_lenght = int(input("Type the minimum lenght of your password: "))
    len_spec = int(input("How many special characters: "))
    len_num = int(input("How many numbers: "))

    # ensure to show the error messag when lenght of numbers and special characters are more than the password lenght
    if min_lenght < len_spec + len_num:
        print("Error: Special characters and numbers exceed the password length.")
    else:
        len_letters = min_lenght - (len_spec + len_num)

        # randomly selects the letters
        random_letters = random.choices(letters, k=len_letters)
        # randomly selects the numbers
        random_num = random.choices(num_list, k=len_num)
        # randomly selects the special characters
        random_special = random.choices(special_char, k=len_spec)

        single_list = random_letters + random_num + random_special

        
        random.shuffle(single_list)

        password = "".join(map(str, single_list))

        print(password)

if __name__ == "__main__":
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_char = ["!", "@", "#", "$", "%"]
    password_generator(letters, num_list, special_char)
