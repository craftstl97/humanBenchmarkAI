import time
import pyautogui
from PIL import Image, ImageGrab

def start():
    '''
    Inputs: None
    Outputs: None

    Automates the reaction time test:

    The test runs 5 times, then displays the results
    each test is a red screen, followed by a flash of green, then a blue continue screen
    do nothing on red, click green as fast as possible, click blue at your leisure
    '''
    print("Selecting Reaction Time test")
    pyautogui.click(x=680, y=400)
    time.sleep(1)

    print("Beginning Test")
    pyautogui.click(x=980,y=300)

    for x in range(5):
        print("Scanning for green")
        react()
        print("Test", x+1 , "complete")
        time.sleep(3)
        pyautogui.click(x=980,y=300)

def get_pixel_color(x,y):
    '''
    Inputs: x,y coordinates of the pixel to test
    Outputs: the color of the pixel in that space
    '''
    screen = ImageGrab.grab(bbox = (x,y,x+1,y+1))
    return screen.getpixel((0,0))
    

def react():
    '''
    Inputs: None
    Outputs: None

    Scans the window for green and clicks (980,300)
    when it sees green, then exits
    '''
    while True:
        current_color = get_pixel_color(200,200)
        print(current_color)
        if current_color[1] >= 150:
            pyautogui.click(x=980,y=300)
            return



    

