# Level 1: Basic XML Reading with lxml
# Goal: Parse a simple XML file and extract elements using lxml.
# Note: You may need to run `pip install lxml` in your terminal first.

import os
from lxml import etree

input_file = "level1_basic.xml"

print(f"--- Reading data from {input_file} ---")

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
else:
    try:
        # Parse the XML file
        tree = etree.parse(input_file)
        # Get the root element (in this case, <book>)
        root = tree.getroot()
        
        print(root)
        print(f"Root Element Tag: {root.tag}\n")
        
        # Iterate through the children of the root and print their tags and text
        for child in root:
            print(f"{child.tag.capitalize()}: {child.text}")
            
    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML: {e}")
    except ImportError:
        print("Error: The 'lxml' library is not installed. Please run 'pip install lxml' in your terminal.")
