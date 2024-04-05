import time
import pyautogui
from PIL import Image, ImageGrab
import pytesseract

tpath = "C:/Users/637817/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

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
    pyautogui.click(x=680, y=700)
    time.sleep(5)

    # Zooming In - The engine struggles to identify certain characters when zoomed out
    pyautogui.click(x=840, y=500)
    print("Zooming in")
    pyautogui.keyDown('ctrl')
    for x in range(4):
        pyautogui.press('+')
    pyautogui.keyUp('ctrl')

    # click start
    print('Clicking Start')
    pyautogui.click(x=960, y=720)

    # Main loop: 
    # 1) get number
    # 2) wait for field to appear
    # 3) type the number in the box
    # 4) Hit Enter 
    # 5) Click next
    for n in range(60):
        time.sleep(1)
        # 1) process image to text
        number = get_number(n)    
        print("Text Detected:\n",number)
        # 2) wait
        wait_for_prompt()
        # 3) type the number using pyautogui.write()
        print('\n Typing number')
        pyautogui.write(number, interval=0.05)
        print('Done')
        time.sleep(0.2)
        # 4) Hit Enter
        pyautogui.press('enter')
        time.sleep(1)
        # 5) Click Next 
        pyautogui.click(x=960, y=720)

def wait_for_prompt():
    '''
    Inputs: None
    Outputs: None

    Looks for the text "What was the number?" on screen
    if it sees it then it returns, otherwise it calls itself
    '''

    image = ImageGrab.grab(bbox = (100,300,1621,751))
    #image.show() # uncomment for testing purposes
    #input() # uncomment with the above line to pause to close the screenshot
    text = pytesseract.image_to_string(image)
    if "What was the number?" not in text:
        wait_for_prompt()
    
def get_number(n):
    ''' 
    Inputs: Level -> int
    Outputs: Text to type -> String
    
    Takes a screenshot and returns the number displayed as a string
    '''
    off = n*50
    if off > 750:
        off = 750
    image = ImageGrab.grab(bbox = (800-off,300,1040+off,601))
    image = image.convert('L') # Convert to grayscale
    image = image.point(lambda p: p > 200 and 255) # convert grayscale to binary for maximum accuracy
    # image.show() # uncomment for testing purposes
    # convert to string, config to only look for digits
    return pytesseract.image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=0123456789')