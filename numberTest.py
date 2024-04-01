import time
import pyautogui
from PIL import Image, ImageGrab
import pytesseract

tpath = "C:/Users/637817/AppData/Local/Programs/Tesseract-OCR"

def start(tesseractPath = tpath):
    '''
    Inputs: Path to tesseract-OCR executable -> String
    Outputs: None

    Automates the Number Memory test:

    This test runs indefinitely, generating a number of length n on the screen for a set amount of time.
    The user then has to type the number into the provided box, press enter, and click a button
    to continue.

    The AI will have to see the number, convert it from an image to a string, then input
    that string using the keyboard. We will need an new python library for this task.

    Note: In order to run this task, an extra parameter needs to be entered "Path to tesseract OCR"
    as the path will be different depending on which computer is running the code.
    '''
    # Set up tesseract
    pytesseract.pytesseract.tesseract_cmd = tesseractPath

    
    # Start the test


def get_num(x1,y1,x2,y2):
    ''' 
    Inputs: four numbers indicating the corners of the bounding box
    Outputs: number -> String
    
    Takes a screenshot and returns the number displayed as a string
    The bounding box will naturally grow as the number gets larger, to give tesseract
    the best chance at getting the right answer, we won't give it more than it needs
    '''

    image = ImageGrab.grab(bbox = (x1,y1,x2,y2))
    return pytesseract.image_to_string(image)