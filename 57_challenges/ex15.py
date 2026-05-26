# Create a simple program that validates user login credentials.
# The program must prompt the user for a username and password. 
# The program should compare the password given by the user to a known password.
# If the password matches, the program should display “Welcome!”. 
# If it doesn’t match, the program should display “I don’t know you.”


user_name = input("Type User Name: ")
password = input("Type your password: ")

saved_password = "User@123"

if password == saved_password:
    print(f"Welcome {user_name}!")
else:
    print(f"I don't know you! Please type the correct password and try again.")


