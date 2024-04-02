# This is the driver program for the human benchmark program
# other files will be added later on in the project for other activities

# Essential imports - Be sure to install the pyautogui package detailed in requirements.txt
import webbrowser
import time
import pyautogui

# Import activity functions here
import reflexTest
import sequenceTest
import numberTest
import typingTest

activities = ['Reaction Time', 'Sequence Memory', 'Aim Trainer', 
              'Number Memory', 'Verbal Memory', 'Chimp Test',
              'Visual Memory', 'Typing Speed']

def welcome():
    '''
    Input: None
    Returns: Activity -> string

    Starting interactions with the user:
    1) Asks which test they want to automate (Tests still in implementation phase)
    2) Asks if they intend to log in to save progress
        a) if yes: prompts for login credentials
    3) Opens the web page and automates the activity
    '''

    # Greeting and disclaimer
    print("Welcome to Human Benchmark!")
    print("""
          This program is intended to be used 
          as a learning experience for myself,
          and not as a way to cheat at human benchmark.
          
          I am making this available to the public to 
          show my portfolio, not for malicious use.
          """)
    
    # Take input of the activity to automate
    print("Now lets get started!\n")
    print("Which test would you like to automate?")
    [print(a) for a in activities]
    choice = input('\n')


    # Check if the activity is implemented/exists
    while choice.lower() not in (a.lower() for a in activities):
        print("\nSorry! That activity is not implemented.\n")
        print("Please choose from the list of activities.")
        [print(a) for a in activities]
        choice = input('\n')

    # Prompt the user to log in if they would like
    saveProgress = input("Would you like to log in? (Y/N)")
    if saveProgress.lower() == 'y':
        print("OK! Please enter your username and password.")
        username = input('Username:')
        password = input('Password:')


    # launch the website and wait for it to load
    webbrowser.get('windows-default').open_new("https://humanbenchmark.com")
    time.sleep(5)

    # log in if the user chose to do so
    if saveProgress.lower() == 'y':
        login(username, password)

    # send the activity choice back to main
    return choice
    

def login(username, password):
    '''
    Input: username -> string
           password -> string
    Returns: None

    Inputs username and password into the site and navigates back to the main page
    '''
    print("Logging in with Username:", username, 'Password:', password)
    print('login currently not supported')

if __name__ == "__main__":
    # Executes main
    activity = welcome()
    print("Beginning automation\n")
    
    # Select the Window
    print('Selecting window')
    pyautogui.moveTo(x=980,y=340)
    pyautogui.leftClick()
    time.sleep(1)

    # Zoom out for maximum screen space
    print("Zooming out")
    pyautogui.keyDown('ctrl')
    for x in range(16):
        pyautogui.press('-')
    for x in range(2):
        pyautogui.press('+')
    pyautogui.keyUp('ctrl')
    time.sleep(1)

    print("Scrolling to options")
    # Navigate to the page
    pyautogui.scroll(-400)
    time.sleep(1)
    
    if activity.lower() == 'reaction time':
        print("Automating Reaction Time Test")
        reflexTest.start()

    if activity.lower() == 'sequence memory':
        print("Automating Sequence Memory Test")
        sequenceTest.start()

    # Aim trainer

    if activity.lower() == 'number memory':
        print("Automating Number Memory Test")
        tesseract = input("Enter path to tesseract-OCR")
        numberTest.start(tesseract)

    # Verbal Memory
        
    # Chimp Test
        
    # Visual Memory
        
    # Typing Speed
    if activity.lower() == 'typing speed':
        print("Automating Typing Speed Test")
        typingTest.start()