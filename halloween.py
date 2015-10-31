#!/usr/bin/python
from sense_hat import SenseHat
import time
import os
from PIL import Image

def load_image_pixels(file_path):
    if not os.path.exists(file_path):
        raise IOError('%s not found' % file_path)
    img = Image.open(file_path).convert('RGB').rotate(90)
    pixel_list = list(map(list, img.getdata()))
    return pixel_list

def scroll_image(sense, file_path, count, scroll_speed=0.1):
    previous_rotation = sense.rotation
    sense.rotation = 270
    image_pixels = load_image_pixels(file_path)
    # need to scroll a 64 pixel image, but starting and ending with blank pixels
    dummy_colour = [0, 0, 0]
    string_padding = [dummy_colour] * 64
    letter_padding = [dummy_colour] * 8
    scroll_pixels = []
    scroll_pixels.extend(string_padding)
    for dummy in range(count):
        scroll_pixels.extend(image_pixels)
        scroll_pixels.extend(string_padding)
    scroll_pixels.extend(string_padding)

    # Shift right by 8 pixels per frame to scroll
    scroll_length = len(scroll_pixels) // 8
    for i in range(scroll_length-8)[::-1]:
        start = i * 8
        end = start + 64
        sense.set_pixels(scroll_pixels[start:end])
        time.sleep(scroll_speed)

    sense.rotation = previous_rotation

sense = SenseHat()
sense.set_rotation(180)
while True:
    red = (255, 0, 0)
    orange = (255, 165, 0)
    green = (0, 255, 0)
    purple = (128,0,128)
    scroll_image(sense, "ghost.png", 4)
    sense.show_message("Happy Halloween!", text_colour=orange)
    scroll_image(sense, "pumpkin.png", 4)
    sense.show_message("Have a spooky time!", text_colour=purple)
    scroll_image(sense, "monster.png", 4)

