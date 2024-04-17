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
    pyautogui.click(x=960, y=400)
    time.sleep(1)

    # Click the start button
    print("Beginning Test")
    pyautogui.click(x=940,y=450)
    
    time.sleep(0.25)
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

    # Screenshot the game space
    image = ImageGrab.grab(bbox = (840,250,1041,451))

    # search screenshot for the target
    # searching left to right, bottom to top

    for x in range(0,200,5):
        for y in range(0,200,5):
            pyautogui.moveTo(x+840, y+250)
            current_color = get_pixel_color(x,y)
            if current_color[1] >= 200:
                return x+840, y+250

    



    return findTarget()