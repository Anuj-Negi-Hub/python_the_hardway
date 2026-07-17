'''
Create a program that determines the complexity of a given password based on these rules:
• A very weak password contains only numbers and is fewer than eight characters.
• A weak password contains only letters and is fewer than eight characters.
• A strong password contains letters and at least one number and is at least eight characters.
• A very strong password contains letters, numbers, and special characters and is at least eight characters.

Example Output
The password '12345' is a very weak password.
The password 'abcdef' is a weak password.
The password 'abc123xyz' is a strong password.
The password '1337h@xor!' is a very strong password.
'''

def passwordValidator(password):
    has_digit = False
    has_special = False
    has_letter = False
    
    password_len = len(password)
    special = "@#$%&!*?"
    
    for ch in password:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True
        
    if has_digit and password_len < 8:
        print(f"The password {password} is a very weak password.")
    elif has_letter and password_len < 8:
        print(f"The password {password} is a weak password.")
    elif has_digit and has_letter and not has_special and password_len >= 8:
        print(f"The password {password} is a strong password.")
    elif has_digit and has_letter and has_special and password_len >= 8:
        print(f"The password {password} is a very strong password.")
    else:
        print("Password does not match any category.")

password = input("Type your password: ")
passwordValidator(password)