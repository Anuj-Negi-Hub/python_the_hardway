import pygame
import requests
from io import BytesIO

# ---------- INIT ----------
pygame.init()           #This initialized all the modules that are imported in this file
WIDTH, HEIGHT = 800, 600        #width and height of the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #creating a game screen with the given width and height
clock = pygame.time.Clock()

# ---------- FETCH CAT FROM API ----------
api_url = "https://api.thecatapi.com/v1/images/search"      #url for the searching the image

image_url = requests.get(api_url).json()[0]["url"] #Getting the actual image url
img_data = requests.get(image_url).content  #fetch the raw bites of the image
# print(img_data)

cat_img = pygame.image.load(BytesIO(img_data)).convert_alpha()   #optimize the image pixel format for faster rendering

# ---------- AUTO SCALE BASE SIZE ----------
# Resize large images to a manageable base size
MAX_SIZE = 200  # max size of image (width/height)   

w, h = cat_img.get_size()       #provide the width and height of the image
scale_factor = min(MAX_SIZE / w, MAX_SIZE / h)  #finding the scale factor of the images that is minimum value of width or height

# print(scale_factor)

base_size = (int(w * scale_factor), int(h * scale_factor))    #new width and height of the image 


cat_img = pygame.transform.smoothscale(cat_img, base_size) #resize the surface of the provided image to the given pixel size

# ---------- HELPERS ----------
def scale_image(img, percent):
    w = int(img.get_width() * percent / 100)
    h = int(img.get_height() * percent / 100)
    return pygame.transform.smoothscale(img, (w, h))

def to_pygame(x, y):
    return int(WIDTH/2 + x), int(HEIGHT/2 - y)

def draw_gradient(surface):
    # simple vertical gradient
    for y in range(HEIGHT):
        color = (135 - y//10, 206 - y//10, 235)  # sky-like gradient
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

# ---------- LOGIC ----------
start = (-150, -117)
end = (188, 135)

scale = 50
progress = 0
direction = 1
moves = 0

running = True
while running:
    draw_gradient(screen)  # nicer background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if moves < 2:
        progress += 0.01

        if progress >= 1:
            progress = 0
            direction *= -1
            moves += 1

        if direction == 1:
            x = start[0] + (end[0] - start[0]) * progress
            y = start[1] + (end[1] - start[1]) * progress
        else:
            x = end[0] + (start[0] - end[0]) * progress
            y = end[1] + (start[1] - end[1]) * progress

        if scale < 100:
            scale += 0.15  # smoother growth

    else:
        x, y = end
        scale = 100

    cat_scaled = scale_image(cat_img, scale)

    px, py = to_pygame(x, y)
    rect = cat_scaled.get_rect(center=(px, py))
    screen.blit(cat_scaled, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()