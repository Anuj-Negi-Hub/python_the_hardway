import os

input_file = "level3_sales.txt"
output_file = "level3_report.txt"

sales_data = {}
errors_found = 0

print(f"--- Analyzing sales data from {input_file} ---")

# Check if file exists before trying to open it
if not os.path.exists(input_file):
    print(f"Error: The file '{input_file}' does not exist.")
else:
    try:
        with open(input_file, 'r') as file:
            header = file.readline().strip().split(',')
            # print(header)
            print(f"Found columns: {header}")

    except ValueError:
                    print(f"Warning: Invalid number format on line {line_num} for product '{product}'. Skipping.")
                    errors_found += 1