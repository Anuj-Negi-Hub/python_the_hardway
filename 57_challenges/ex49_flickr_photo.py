'''
Create a program with a graphical interface that takes in a
search string and displays photographs that match that
search string. Use Flickr’s public photo feed at
https://www.flickr.com/services/feeds/docs/photos_public/ as your
service.
Example Output
Your program should display the photographs like this:
    [Photo Gallery]
'''

import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# -----------------------------
# Function to search Flickr
# -----------------------------
def search_photos():
    # Remove previously displayed images
    for widget in image_frame.winfo_children():
        widget.destroy()

    search_term = entry.get().strip()

    if search_term == "":
        messagebox.showerror("Error", "Please enter a search term.")
        return

    url = "https://www.flickr.com/services/feeds/photos_public.gne"

    params = {
        "tags": search_term,
        "format": "json",
        "nojsoncallback": 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        photos = data["items"][:9]      # Display first 9 images

        if not photos:
            messagebox.showinfo("No Results", "No photos found.")
            return

        image_references.clear()

        row = 0
        column = 0

        for photo in photos:

            image_url = photo["media"]["m"]

            image_response = requests.get(image_url)
            image_response.raise_for_status()

            image = Image.open(BytesIO(image_response.content))

            image.thumbnail((180, 180))

            photo_image = ImageTk.PhotoImage(image)

            image_references.append(photo_image)

            label = tk.Label(image_frame, image=photo_image)
            label.grid(row=row, column=column, padx=5, pady=5)

            column += 1

            if column == 3:
                column = 0
                row += 1

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Flickr Photo Search")
root.geometry("620x650")

# -----------------------------
# Search Frame
# -----------------------------
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

label = tk.Label(top_frame, text="Search:")
label.pack(side=tk.LEFT)

entry = tk.Entry(top_frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

button = tk.Button(
    top_frame,
    text="Search",
    command=search_photos
)
button.pack(side=tk.LEFT)

# -----------------------------
# Image Frame
# -----------------------------
image_frame = tk.Frame(root)
image_frame.pack()

# Prevent images from being garbage collected
image_references = []

root.mainloop()