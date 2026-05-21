import json
from lxml import etree

with open("exercise3.json", "r") as f:
    topics = json.load(f)

map_root = etree.Element("map", title="AI Reference Guide")

for topic in topics:
    # 1. Create the main topicref
    topicref = etree.SubElement(
        map_root, 
        "topicref", 
        href=topic["href"]
    )
    
    # 2. Create the topicmeta container inside the topicref
    topicmeta = etree.SubElement(topicref, "topicmeta")
    
    # 3. Add the navtitle element (alternative to the navtitle attribute)
    navtitle = etree.SubElement(topicmeta, "navtitle")
    navtitle.text = topic["title"]
    
    # 4. Add author element
    author = etree.SubElement(topicmeta, "author")
    author.text = topic["author"]
    
    # 5. Add shortdesc element
    shortdesc = etree.SubElement(topicmeta, "shortdesc")
    shortdesc.text = topic["description"]

tree = etree.ElementTree(map_root)
tree.write("exercise3_map.ditamap", pretty_print=True, xml_declaration=True, encoding="UTF-8")
print("Saved to exercise3_map.ditamap")
