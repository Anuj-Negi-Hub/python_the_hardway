# Level 3: Advanced File Handling - Parsing, Error Handling, and Formatted Output
# This script reads a structured text file (CSV format), parses it, handles potential errors (like invalid numbers),
# calculates total sales per product, and writes a formatted report.

import os

input_file = "level3_sales.txt"         #creating variables to store the input file name
output_file = "level3_report.txt"       #creating variable to store output file name 

sales_data = {}             #creating an empty variable to store the sales value as dictionary (kye: value)
errors_found = 0            #creating a variable to store the error count

print(f"--- Analyzing sales data from {input_file} ---")

# Check if file exists before trying to open it
if not os.path.exists(input_file):
    print(f"Error: The file '{input_file}' does not exist.")        #print the error if input file does not exist
else:
    try:
        with open(input_file, 'r') as file:
            #read the first line of the file, remove whitespaces, seperate line with comma, and store as a list to the variable
            header = file.readline().strip().split(',')     
            # print(header)
            print(f"Found columns: {header}")   #print the first line
            
            line_num = 1            #count of the line . Already the line count is 1
            for line in file:       #for loop to read each line one-by-one
                line_num += 1       #increase the line by 1 
                parts = line.strip().split(',')     #store line as list
                
                if len(parts) != 4:      #condition to executre when parts (list) is not equal to 4  
                    print(f"Warning: Line {line_num} is malformed. Skipping.")  #print a message with the error
                    errors_found += 1   #increase the error count by 1 and store the error count
                    continue            #continue the code even if the error exists 
                
                date, product, quantity_str, price_str = parts      #unpacking and storing each list item in the parts variable to the seperate variables
                
                try:
                    quantity = int(quantity_str)        #converting to integer
                    price = float(price_str)            #converting to float
                    total_value = quantity * price      #calculating the total value
                    
                    if product in sales_data:           #condition to execute when product is there in sales_data
                        sales_data[product]['quantity'] += quantity    # increase the product quantity
                        sales_data[product]['revenue'] += total_value  #increase the total revenue
                    else:
                        sales_data[product] = {'quantity': quantity, 'revenue': total_value}        #if product is not in sales_data, create a disctionary to store the product information
                        
                except ValueError:          #if there is a mismatch in part lenght, then it will be a value error  
                    print(f"Warning: Invalid number format on line {line_num} for product '{product}'. Skipping.")
                    errors_found += 1   #increase the error by 1

        print(f"\n--- Generating Report to {output_file} ---")      #printing message
        with open(output_file, 'w') as file:                        #opening the output file and storing it in file variable
            file.write("=== SALES SUMMARY REPORT ===\n")            #writing to the file. THis will be the first line
            file.write(f"{'Product':<15} | {'Total Sold':<10} | {'Total Revenue'}\n")   #second line with "|" seperator and space of 15, 10
            file.write("-" * 50 + "\n")         #write "-" 50 times
            
            for product, data in sorted(sales_data.items()):    
                file.write(f"{product:<15} | {data['quantity']:<10} | ${data['revenue']:.2f}\n")    #write the remaining data in the file
                
            file.write("-" * 50 + "\n")
            if errors_found > 0:    #execute this condition when error is more than 0   
                file.write(f"Note: {errors_found} errors/invalid lines were skipped during processing.\n")
                
        print("Report successfully generated!")

    except IOError as e:        #input output error in any case if file cannot be opened or found as save that error in e variable
        print(f"An I/O error occurred: {e}")
    except Exception as e:      #handling any other erros except the one mentioned above
        print(f"An unexpected error occurred: {e}")