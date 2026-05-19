# Level 3: Advanced JSON Handling - Parsing, Validation, and Aggregation
# Goal: Parse complex JSON, handle data type errors safely, and create a summary report JSON.

import json     #importing json module for reading, writing, parsing json data
import os       #importing os module to interact with operating system

input_file = "level3_sales.json"        #storing input file name
output_file = "level3_summary.json"     #stroing output file name

if not os.path.exists(input_file):      #if condition to check if input file exists
    print(f"Error: {input_file} not found.")    #if not exist, print error message
else:                                   #if file exists, else condition with execute
    try:                                #error handling try block
        with open(input_file, 'r') as file:     #open input file as file
            store_data = json.load(file)        #parse input file data to python objects

        # Extract top-level info
        store_id = store_data.get('store_id', 'Unknown Store')      #fetching data of store_id and storing it in store_id. If no data in store_id, return Unknown Store
        location = store_data.get('location', 'Unknown Location')   #fetching data of location and storing it in location. If no data in location, return Unknown Location
        transactions = store_data.get('transactions', [])           #fetching data of transactions and storing it in transactions. If no data in transactions, return empty list
        
        print(f"--- Processing Sales for {store_id} ({location}) ---")
        
        total_revenue = 0.0         #storing total revenue as float
        successful_tx = 0           #storing the count of successful tx
        failed_tx = 0               #storing the countof failed tx 
        items_sold = {}             #storing the quantity of item old in empyt dictionary

        # Process each transaction safely
        for tx in transactions:         #for loop to access each item in transactions
            tx_id = tx.get('tx_id', 'Unknown')   #fetch tx_id and store it in tx_id. Unknown if no data
            item = tx.get('item', 'Unknown')     #fetch item and store it in item. Unknown if no data
            
            try:                #try block to verify the formats
                # Try to convert values to proper numbers (will fail if qty is a string like "four")
                qty = int(tx.get('qty', 0))     #fetching the quantity details and converting to integer. Storing to qty. if no data, return 0
                price = float(tx.get('price', 0.0)) #fetching the price details and converting to float. Storing to price. if no data, return 0.0
                
                revenue = qty * price       #calculate the revenue
                total_revenue += revenue    #store the total_revenue
                successful_tx += 1          #increae the transaction by 1 if successful
                
                # Keep track of quantities sold per item
                items_sold[item] = items_sold.get(item, 0) + qty    #count the quantity of sold items
                                
            except ValueError:      #except block to handle errors if the format is not corret
                print(f"Warning: Transaction {tx_id} contains invalid number formats. Skipping.") #Print the error message
                failed_tx += 1      #increase the failed transaction by 1

        # Create a dictionary for our final summary report
        summary_report = {              #creating the dictionary for final report and storing it in summary report
            "store": store_id,
            "metrics": {
                "total_revenue": round(total_revenue, 2),
                "successful_transactions": successful_tx,
                "failed_transactions": failed_tx
            },
            "item_breakdown": items_sold
        }

        # Save the summary report to a new JSON file
        with open(output_file, 'w') as file:        #opening output file in 
            json.dump(summary_report, file, indent=4)   #dumping all the data to file and converting python object to json format
            
        print("\n--- Summary ---")              #print message
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Success: {successful_tx} | Failed: {failed_tx}")
        print(f"Summary saved to {output_file}")

    except json.JSONDecodeError as e:           #except block: print message if the format of json is invalid 
        print(f"Error: Invalid JSON format. {e}")
    except Exception as e:                      # print message if there is any other error occurs
        print(f"An unexpected error occurred: {e}")
