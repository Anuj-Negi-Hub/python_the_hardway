# Exercise 3: Merge Two PDFs

# Goal;
    # Combine two PDF files into one.

# Skills Learned:
    # Writing PDFs
    # Combining documents

import time
from pypdf import PdfWriter

start_time = time.time()
print(start_time)
merger = PdfWriter()
print("Adding the first pdf file...")
merger.append(r"D:\PDFs\page_1.pdf")

print("Adding the second pdf file...")
merger.append(r"D:\PDFs\page_2.pdf")

print("Writing both merged file...")
merger.write(r"D:\PDFs\merged_copy.pdf")
merger.close()

end_time = time.time()
print(end_time)
total_time = end_time- start_time

print(f"The total time taken to merge the both pdf files is {total_time:.2f} seconds.")

print("PDFs merged successfully")

