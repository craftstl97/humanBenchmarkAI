import time
import pyautogui
from PIL import Image, ImageGrab

def start():
    '''
    Inputs: None
    Outputs: None

    Automates the Sequence Memory test:

    This test runs indefinitely, generating a pattern of length n on a 3x3 grid where
    n is the number of correct attempts. The user then has to repeat that pattern on the
    grid in the correct order. 

    The AI will have to add the full sequence to a list, then play that list back.
    Each time, the list will have to grow to fit the next move.
    '''

    print("Selecting Sequence Memory test")
    pyautogui.click(x=960, y=400)
    time.sleep(1)

    # Click the start button
    print("Beginning Test")
    pyautogui.click(x=940,y=450)
    
    time.sleep(0.25)
    n = 1
    while ImageGrab.grab(bbox = (840,450,841,451)).getpixel((0,0))[2] >= 100:
        # Test is still going
        print('Round', n)
        sequence = []

        # Identify the whole sequence
        for square in range(n):
            active = get_active_square()

            # there should be no immediate repeats
            if square >= 1:
                while active == sequence[square - 1]:
                    active = get_active_square()

            print("Square", active, 'is lit')
            sequence.append(active)

        # Give some time for the test to start accepting input 
        time.sleep(0.5)
        
        # Input the sequence
        for i in sequence:
            print('Clicking', i)
            click_square(i)
            time.sleep(0.1)
        
        # increment level counter
        n += 1

    print("Testing Complete")
    


def get_active_square():
    '''
    Inputs: None
    Outputs: Active square -> Int

    Looks at each of the nine squares, and returns as soon as it finds one that is white
    if none are white, restart
    '''
    image = ImageGrab.grab(bbox = (840,250,1041,451))

    if image.getpixel((0,200))[2] >= 240:
        return 1
    if image.getpixel((100,200))[2] >= 240:
        return 2
    if image.getpixel((200,200))[2] >= 240:
        return 3
    if image.getpixel((0,100))[2] >= 240:
        return 4
    if image.getpixel((100,100))[2] >= 240:
        return 5
    if image.getpixel((200,100))[2] >= 240:
        return 6
    if image.getpixel((0,0))[2] >= 240:
        return 7
    if image.getpixel((100,0))[2] >= 240:
        return 8
    if image.getpixel((200,0))[2] >= 240:
        return 9
    return get_active_square()
    

    if ImageGrab.grab(bbox = (840,450,841,451)).getpixel((0,0))[2] >= 240:
        return 1 
    if ImageGrab.grab(bbox = (940,450,941,451)).getpixel((0,0))[2] >= 240:
        return 2
    if ImageGrab.grab(bbox = (1040,450,1041,451)).getpixel((0,0))[2] >= 240:
        return 3
    if ImageGrab.grab(bbox = (840,350,841,351)).getpixel((0,0))[2] >= 240:
        return 4
    if ImageGrab.grab(bbox = (940,350,941,351)).getpixel((0,0))[2] >= 240:
        return 5
    if ImageGrab.grab(bbox = (1040,350,1041,351)).getpixel((0,0))[2] >= 240:
        return 6
    if ImageGrab.grab(bbox = (840,250,841,251)).getpixel((0,0))[2] >= 240:
        return 7
    if ImageGrab.grab(bbox = (940,250,941,251)).getpixel((0,0))[2] >= 240:
        return 8
    if ImageGrab.grab(bbox = (1040,250,1041,251)).getpixel((0,0))[2] >= 240:
        return 9
    return get_active_square()

def click_square(square):
    '''
    Inputs: index of square -> Int
    Outputs: None

    Calls the click function to click the corresponding square
    '''
    if square == 1:
        pyautogui.click(x=840, y=450)
    elif square == 2:
        pyautogui.click(x=940, y=450)
    elif square == 3:
        pyautogui.click(x=1040, y=450)
    elif square == 4:
        pyautogui.click(x=840, y=350)
    elif square == 5:
        pyautogui.click(x=940, y=350)
    elif square == 6:
        pyautogui.click(x=1040, y=350)
    elif square == 7:
        pyautogui.click(x=840, y=250)
    elif square == 8:
        pyautogui.click(x=940, y=250)
    elif square == 9:
        pyautogui.click(x=1040, y=250)
    