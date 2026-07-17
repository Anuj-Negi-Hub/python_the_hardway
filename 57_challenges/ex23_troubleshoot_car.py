'''
Create a program that walks the user through troubleshooting issues with a car. Use the following decision tree to build the system:
Example Output
Is the car silent when you turn the key? y
Are the battery terminals corroded? n
The battery cables may be damaged.
Replace cables and try again.
'''
#troubleshooting the faulty car
user_input = input("Is the car silent when you turn the key? Answer only y or n: ").lower()

if user_input == "y":
    bat_ter = input("Are the battery terminals corroded? ")
    if bat_ter == "y":
        print("Clean terminals and try starting again.")
    elif bat_ter == "n":
        print("Replace cables and try again.")
    else:
        print("Try again. You did not type the correct input as y or n.")
    
elif user_input == "n":
    noise_check = input("Does the car make a clicking noise?")
    if noise_check == "y":
        print("Replace the battery.")
    elif noise_check == "n":
        car_crank = input("Does the car crank up but fail to start?")
        if car_crank == "y":
            print("Check spark plug connections.")
        elif car_crank == "n":
            engine_start = input("Does the engine start and then die?")
            if engine_start == "y":
                fuel_check = input("Does your car have fuel injection?")
                if fuel_check == "y":
                    print("Get it in for service.")
                elif fuel_check == "n":
                    print("Check to ensure the choke is opening and closing.")
                else:
                   print("Try again. You did not type the correct input as y or n.")
            elif engine_start == "n":
                print("Show it to the mechanic.")
            else:
                print("Try again. You did not type the correct input as y or n.")

        else:
            print("Try again. You did not type the correct input as y or n.")

    else:
        print("Try again. You did not type the correct input as y or n.")
        
else:
    print("Try again. You did not type the correct input as y or n.")