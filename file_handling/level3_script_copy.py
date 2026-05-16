# Advanced File Handling Project
# Reads sales data from a CSV file
# Handles errors safely
# Generates formatted sales report

import os

input_file = "level3_sales.txt"
output_file = "level3_report.txt"

sales_data = {}
errors_found = 0

print(f"\n--- Analyzing sales data from {input_file} ---")

# Check if file exists
if not os.path.exists(input_file):
    print(f"Error: '{input_file}' does not exist.")

else:
    try:
        # Open input file
        with open(input_file, "r") as file:

            # Read header line
            header = file.readline().strip().split(",")

            print(f"Found columns: {header}")

            line_num = 1

            # Read remaining lines
            for line in file:

                line_num += 1

                # Skip empty lines
                if line.strip() == "":
                    print(f"Warning: Empty line at {line_num}. Skipping.")
                    errors_found += 1
                    continue

                parts = line.strip().split(",")

                # Check correct number of columns
                if len(parts) != 4:
                    print(f"Warning: Line {line_num} is malformed. Skipping.")
                    errors_found += 1
                    continue

                # Unpack values
                date, product, quantity_str, price_str = parts

                try:
                    # Convert values
                    quantity = int(quantity_str)
                    price = float(price_str)

                    # Check negative values
                    if quantity < 0 or price < 0:
                        print(f"Warning: Negative values on line {line_num}. Skipping.")
                        errors_found += 1
                        continue

                    # Calculate total sale
                    total_value = quantity * price

                    # Update existing product
                    if product in sales_data:

                        sales_data[product]["quantity"] += quantity
                        sales_data[product]["revenue"] += total_value

                    # Add new product
                    else:
                        sales_data[product] = {
                            "quantity": quantity,
                            "revenue": total_value
                        }

                # Handle invalid numbers
                except ValueError:
                    print(f"Warning: Invalid number format on line {line_num}. Skipping.")
                    errors_found += 1

        # Generate output report
        print(f"\n--- Generating Report to {output_file} ---")

        try:
            with open(output_file, "w") as file:

                file.write("=== SALES SUMMARY REPORT ===\n\n")

                file.write(f"{'Product':<15} | {'Total Sold':<12} | {'Total Revenue'}\n")

                file.write("-" * 55 + "\n")

                # Sort products alphabetically
                for product, data in sorted(sales_data.items()):

                    file.write(
                        f"{product:<15} | "
                        f"{data['quantity']:<12} | "
                        f"${data['revenue']:.2f}\n"
                    )

                file.write("-" * 55 + "\n")

                file.write(f"Errors Skipped: {errors_found}\n")

            print("Report successfully generated!")

        # Handle writing errors
        except PermissionError:
            print(f"Error: Permission denied while writing '{output_file}'.")

        except IOError as e:
            print(f"Output file error: {e}")

    # Handle reading permission errors
    except PermissionError:
        print(f"Error: Permission denied while opening '{input_file}'.")

    # Handle file reading errors
    except IOError as e:
        print(f"I/O Error occurred: {e}")

    # Handle unexpected errors
    except Exception as e:
        print(f"Unexpected error occurred: {e}")