# Level 2: Intermediate XML Handling - Modifying and Saving
# Goal: Read an XML file, modify some values (e.g., increase price), and save to a new file.

import os
from lxml import etree

input_file = "level2_data.xml"
output_file = "level2_updated.xml"

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
else:
    try:
        # Parse the existing XML
        tree = etree.parse(input_file)
        root = tree.getroot()
        # print(root.tag)
        
        print("--- Updating Inventory Prices (10% Increase) ---")
        
        # Find all <item> elements
        for item in root.findall('item'):
            name = item.find('name').text
            price_elem = item.find('price')
            
            # Calculate new price
            old_price = float(price_elem.text)
            new_price = old_price * 1.10
            
            # Update the text of the price element
            price_elem.text = f"{new_price:.2f}"
            
            # Add an attribute to indicate it was updated
            item.set("updated", "true")
            
            print(f"Updated {name}: ${old_price} -> ${new_price:.2f}")

        # Save the modified XML tree to a new file
        # pretty_print=True makes the output nicely indented
        tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")
        print(f"\nSaved updated inventory to {output_file}")
        
    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML: {e}")
    except ImportError:
        print("Error: The 'lxml' library is not installed. Please run 'pip install lxml' in your terminal.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
