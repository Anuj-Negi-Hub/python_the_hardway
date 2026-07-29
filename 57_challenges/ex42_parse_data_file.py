'''
Construct a program that reads in the following data file:
Ling,Mai,55900
Johnson,Jim,56500
Jones,Aaron,46000
Jones,Chris,34500
Swift,Geoffrey,14200
Xiong,Fong,65000
Zarnecki,Sabrina,51500

Process the records and display the results formatted as a
table, evenly spaced, as shown in the example output.

Example Output:

Last First Salary
-------------------------
Ling Mai 55900
Johnson Jim 56500
Jones Aaron 46000
Jones Chris 34500
Swift Geoffrey 14200
Xiong Fong 65000
Zarnecki Sabrina 51500
'''

with open("ex42_parse_data_file_input.txt", "r") as file:
    file_text = file.readlines()
    

with open("ex42_parse_data_file_output.txt", "w") as file:
    # Print the table heading
    file.write(f"{'Last Name':<15}{'First Name':<15}{'Salary':>10}" + "\n")
    file.write("-" * 40 + "\n")

    # read one line
    for line in file_text:
        #remove whitespaces before and after the string
        line = line.strip()

        #split the line into three parts
        last_name, first_name, salary = line.split(",")

        file.write(f"{last_name:<15}{first_name:<15}${int(salary):>9,}" + "\n")
    