# Level 1: Basic JSON Reading
# Goal: Load a simple JSON file and print its contents.

import json
import os

input_file = "level1_basic.json"

print(f"--- Reading data from {input_file} ---")

# Ensure the file exists
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
else:
    with open(input_file, 'r') as file:
        # json.load() parses the JSON file and converts it into a Python dictionary
        data = json.load(file)
        
        print("Raw Data (Dictionary):", data)
        print("-" * 20)
        
        # Accessing specific values using keys
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"City: {data['city']}")
