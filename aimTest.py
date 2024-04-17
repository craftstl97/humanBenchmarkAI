import time
import pyautogui
from PIL import Image, ImageGrab

def start():
    '''
    Inputs: None
    Outputs: None

    The aim trainer test tasks the user with clicking a series of targets as fast as possible
    as close to their centers as possible.

    This test runs until 30 targets are clicked and then gives a score based upon speed and accuracy.

    The AI will have to identify the center of each target and click its coordinates as fast as possible.
    '''

    print("Selecting Sequence Memory test")
    pyautogui.click(x=1260, y=400)
    time.sleep(5)

    # The first target is free, right in the center
    print("Beginning Test")
    pyautogui.click(x=920,y=330)

    for x in range(30):
        x, y = findTarget()
        pyautogui.leftClick()
        # add delay if needed, shouldn't be necessary
    
    print("Testing Complete")

def findTarget():
    '''
    Inputs: None
    Outputs: x,y -> Int,Int

    Takes a screenshot, searches for the target within that screenshot, and returns its coordinates
    '''

    x1 = 600
    x2 = 1201
    y1 = 160
    y2 = 531
    # Screenshot the game space
    image = ImageGrab.grab(bbox = (x1,y1,x2,y2))

    # search screenshot for the target
    # searching left to right, bottom to top
    for y in range(0,y2-y1,80):
        for x in range(0,x2-x1,80):
            pyautogui.moveTo(x+x1, y+y1)
            current_color = image.getpixel((x,y))
            print(current_color)
            if current_color[1] >= 150:
                print("Target Found!")
                return x+x1, y+y1

    return findTarget()