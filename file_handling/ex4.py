# Exercise 4 — Count Total Lines

# Goal
# Count number of lines in a file.

# num_line = []

try:
    with open("ex3.txt", "r") as file:
        # for line in file:
        #     print(line.strip())

        line = file.readlines()
        print("Total lines:", len(line))
        
        

except IOError as e:
    print("The file cannot be read.", e)
    


