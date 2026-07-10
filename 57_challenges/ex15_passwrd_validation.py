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

print()
#solving the same problem using function

def val_cred(user_name, password):

    saved_password = "User@123"

    if password == saved_password:
        print(f"Welcome {user_name}!")
    else:
        print(f"I don't know you! Please type the correct password and try again.")

user_name = input("Type User Name: ")
password = input("Type your password: ")
val_cred(user_name, password)


#solve the same problem using class

class Credential():
    def __init__(self, user_name, password):
        self.name = user_name
        self.password = password

    def validate_cred(self):
        saved_password = "User@123"
        
        if self.password == saved_password:
            print(f"Welcome {self.name}!")
        else:
            print(f"I don't know you! Please type the correct password and try again.")

user_name = input("Type User Name: ")
password = input("Type your password: ")

a1 = Credential(user_name, password)

a1.validate_cred()