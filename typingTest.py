import time
import pyautogui
from PIL import Image, ImageGrab
import pytesseract

tpath = "C:/Users/637817/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

def start(tesseractPath = tpath):
    '''
    Inputs: Path to tesseract-OCR executable -> String
    Outputs: None

    Automates the Typing Speed test:

    This test provides a single block of text to be typed as fast as possible. It gives 
    unlimited time to read until you start typing, then calculates your typing speed after you finish.

    The AI will have to see the text, convert it from an image to a string, then input
    that string using the keyboard. We will need an new python library for this task.

    Note: In order to run this task, an extra parameter needs to be entered "Path to tesseract OCR"
    as the path will be different depending on which computer is running the code. To run this on a
    different computer, the tesseract library, and tesseract-OCR must be installed and the path must be
    entered at the top of this file or passed to the function.
    '''
    # Set up tesseract
    pytesseract.pytesseract.tesseract_cmd = tesseractPath
    
    # Start the test
    pyautogui.click(x=1040, y=900)
    time.sleep(5)

    # Zooming In - The engine struggles to identify certain characters when zoomed out
    pyautogui.click(x=840, y=500)
    print("Zooming in")
    pyautogui.keyDown('ctrl')
    for x in range(4):
        pyautogui.press('+')
    pyautogui.keyUp('ctrl')

    # reselect the text box
    pyautogui.click(x=840, y=550)

    # process image to text
    text = get_text()    
    # the model sometimes adds line like characters at the start of the string
    text = text.strip('[\|/]')
    # The model seems to mistake I for |, replace them
    text = text.replace('|','I')
    # Finally, the model appears to mis-count spaces
    text = " ".join(text.split())
    print('Text detected:', text)

    # type the text using pyautogui.write()
    print('\n Typing Text')
    pyautogui.write(text)
    print('Done')


def get_text():
    ''' 
    Inputs: None
    Outputs: Text to type -> String
    
    Takes a screenshot and returns the text displayed as a string
    '''

    image = ImageGrab.grab(bbox = (100,450,1621,751))
    #image.show() # uncomment for testing purposes
    return pytesseract.image_to_string(image)