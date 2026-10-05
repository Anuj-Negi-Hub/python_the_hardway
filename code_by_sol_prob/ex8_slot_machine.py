quarters = int(input("How many quarters Martha has: "))
first = int(input("How many game already played in Machine-1 before martha: "))
second = int(input("How many game already played in Machine-2 before martha: "))
third = int(input("How many game already played in Machine 3 before  martha: "))
machine = int(input("From which machine Martha is going to start play"))

plays = 0

while quarters >= 1:
    quarters = quarters - 1

    if machine == 1:
        first = first + 1
        if first == 35:
            quarters = quarters + 30
            first = 0
        
    elif machine == 2:
        second = second + 1
        if second == 100:
            quarters = quarters + 60
            second == 0
    
    elif machine == 3:
        third  = third + 1
        if third == 10:
            quarters = quarters + 9
            third == 0

    plays = plays + 1
    machine = machine + 1
    if machine == 4:
        machine = 1
print(f"Martha has played {plays} game before see got out of money.")




