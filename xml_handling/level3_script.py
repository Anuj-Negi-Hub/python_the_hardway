# Level 3: Advanced XML Handling - XPath Querying and Building from Scratch
# Goal: Use XPath to find specific data, calculate totals, and build a new summary XML file from scratch.

import os
from lxml import etree

input_file = "level3_catalog.xml"
output_file = "level3_summary.xml"

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
else:
    try:
        tree = etree.parse(input_file)
        print(type(tree))
        
        # 1. Advanced Querying using XPath
        # Find all books that are in stock
        in_stock_books = tree.xpath('//book[@in_stock="true"]')        
        print(f"Found {len(in_stock_books)} books currently in stock.")
        
        # Find all Python books
        python_books = tree.xpath('//book[@category="python"]')
               
        
        total_python_value = 0.0
        for book in python_books:
            title = book.find('title').text
            price = float(book.find('price').text)
            total_python_value += price
            print(f"- {title}: ${price}")
            
        print(f"Total value of Python books: ${total_python_value:.2f}\n")
        
        # 2. Building a New XML Document from Scratch
        print(f"--- Generating Summary Report ---")
        
        # Create the root element
        summary_root = etree.Element("library_summary")
        
        # Create sub-elements
        stats_elem = etree.SubElement(summary_root, "statistics")
        
        in_stock_elem = etree.SubElement(stats_elem, "total_in_stock")
        in_stock_elem.text = str(len(in_stock_books))
            
        python_val_elem = etree.SubElement(stats_elem, "python_books_value")
        python_val_elem.text = f"{total_python_value:.2f}"
        
        # Create a new tree from our root element
        new_tree = etree.ElementTree(summary_root)
        
        # Write the new tree to a file
        new_tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="UTF-8")
        print(f"Saved summary to {output_file}")

    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML: {e}")
    except ImportError:
        print("Error: The 'lxml' library is not installed. Please run 'pip install lxml' in your terminal.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
