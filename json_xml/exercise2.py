import json
from lxml import etree

with open("exercise2.json", "r") as f:
    chapters = json.load(f)

map_root = etree.Element("map", title="Python Advanced Course")

for chapter in chapters:
    # Create the parent <topicref> for the chapter
    chapter_ref = etree.SubElement(
        map_root, 
        "topicref", 
        href=chapter["href"], 
        navtitle=chapter["chapter_title"]
    )
    
    # Loop through the nested 'sections' array
    for section in chapter.get("sections", []):
        # Create a child <topicref> inside the chapter_ref
        etree.SubElement(
            chapter_ref, 
            "topicref", 
            href=section["href"], 
            navtitle=section["title"]
        )

tree = etree.ElementTree(map_root)
tree.write("exercise2_map.ditamap", pretty_print=True, xml_declaration=True, encoding="UTF-8")
print("Saved to exercise2_map.ditamap")
