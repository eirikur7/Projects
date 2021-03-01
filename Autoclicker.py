from time import sleep
from PIL import ImageGrab
import numpy as np
import mouse

 # Coordinates where the notifcation box is located
x = 1366
y = 768

# seconds between each iteration
time_interval = 10

# color white
white = [255, 255, 255]     

while True:
    # Get image and transform it to an array of numbers
    screen = np.array(ImageGrab.grab(bbox=[x, y, x+1, y+1]))[0][0] # use indices to get only one pixel

    # check if the pixel is white
    if screen != white:

        # move mouse to pixel coordinates
        mouse.move(x,y, absolute=True, duration=0)

        # left click
        mouse.click('left')

    # sleep for x amount of time
    sleep(time_interval)
