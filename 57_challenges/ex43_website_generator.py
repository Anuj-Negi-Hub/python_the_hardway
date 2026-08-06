'''
Create a program that generates a website skeleton with the following specifications:
• Prompt for the name of the site.
• Prompt for the author of the site.
• Ask if the user wants a folder for JavaScript files.
• Ask if the user wants a folder for CSS files.
• Generate an index.html file that contains the name of the
site inside the <title> tag and the author in a <meta> tag.

Example Output
Site name: awesomeco
Author: Max Power
Do you want a folder for JavaScript? y
Do you want a folder for CSS? y
Created ./awesomeco
Created ./awesomeco/index.html
Created ./awesomeco/js/
Created ./awesomeco/css/
'''

import os
site_name = input("Site name: ")
author_name = input("Autor name: ")
js_folder = input("Javascript folder: ")
css_folder = input("CSS folder: ")

# create the main website folder
os.mkdir(f"{site_name}")
print(f"Created ./{site_name}")

#print author nam
print(f"Author nbame: {author_name}")

# create index.html folder

with open(f"{site_name}/index.html", "w") as file:
    file.write("<html>\n")
    file.write("<head>\n")
    file.write(f"<title>{site_name}</title>\n")
    file.write(f'<meta name="author" content="{author_name}">\n')
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("</body>\n")
    file.write("</html>\n")

print(f"Created ./{site_name}/index.html")

#create javascript file:

if js_folder.lower() == "y":
    os.mkdir(f"{site_name}/js")
    print(f"Created ./{site_name}/js")

# create cs file folder
if css_folder.lower() == "y":
    os.mkdir(f"{site_name}/css")
    print(f"Created ./{site_name}/css")


