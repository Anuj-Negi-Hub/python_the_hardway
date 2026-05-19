# Your Task

# Write a Python program that:

# Opens the JSON file
# Reads student data
# Calculates:
    # total marks
    # average marks
    # topper name
# Creates a summary dictionary
# Saves summary into: summary.json

import json
import os

input_file = "student.json"
output_file = "student_output.json"

if not os.path.exists(input_file):
    print(f"The {input_file} does not exists.")
else:
    try:
        with open(input_file, "r") as file:
            students = json.load(file)
            # print(store_data)
        
        total_marks = 0
        total_students = 0
        highest_marks = 0
        topper = ""
            
        for student in students:
            name = student.get("name", "Unknown")
            print(name)
            marks = student.get("marks", 0)
            print(marks)   

            try:
                marks = int(marks)   
                total_marks += marks    
                total_students += 1

                #find topper
                if marks > highest_marks:
                    highest_marks   = marks
                    topper = name 

            except ValueError:
                print(f"Invalid marks for {name}: skipping.")

        #calculate average
        average_marks = round(total_marks / total_students, 2) 

        #create summary dictionary
        summary = {
            "total_students": total_students,
            "average_marks": average_marks,
            "topper": topper,
            "highest_marks": highest_marks   
        }

        #save summary json
        with open(output_file, "w") as file:
            json.dump(summary, file, indent=4)
        
        # Print summary
        print("\n--- Student Summary ---")
        print(f"Total Students: {total_students}")
        print(f"Average Marks: {average_marks}")
        print(f"Topper: {topper}")
        print(f"Highest Marks: {highest_marks}")

    
    except json.JSONDecodeError as e:            
        print(f"Error: Invalid JSON format. {e}")
    except Exception as e:                      
        print(f"An unexpected error occurred: {e}") 
        


