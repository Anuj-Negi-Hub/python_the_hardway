import json
from lxml import etree

# 1. Read the JSON data
with open("exercise1.json", "r") as f:
    topics = json.load(f)

# 2. Create the DITA Map root element
# Adding standard DITA DOCTYPE isn't strictly required by lxml to build the tree,
# but it's good practice for DITA.
map_root = etree.Element("map", title="Python Basics Course")

# 3. Loop through JSON and create topicrefs
for topic in topics:
    # Create the <topicref> element and add attributes
    etree.SubElement(
        map_root, 
        "topicref", 
        href=topic["href"], 
        navtitle=topic["title"]
    )

# 4. Save to XML
tree = etree.ElementTree(map_root)
tree.write(
    "exercise1_map.ditamap", 
    pretty_print=True, 
    xml_declaration=True, 
    encoding="UTF-8",
    doctype='<!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "map.dtd">'
)
print("Saved to exercise1_map.ditamap")
