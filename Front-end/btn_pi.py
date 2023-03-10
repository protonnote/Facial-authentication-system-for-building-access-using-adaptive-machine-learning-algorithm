import RPi.GPIO as GPIO
import time
from datetime import date, datetime
        
def btn():

    GPIO.setwarnings(False) 
    
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    
    start = datetime.now()
    
    while True:
        if GPIO.input(14) == GPIO.HIGH:
            print("YES")
            return 0
            # time.sleep(0.3)
        if GPIO.input(4) == GPIO.HIGH:
            print("No")
            return 1
            # time.sleep(0.3)
        cal = datetime.now() - start
        minutes = divmod(cal.total_seconds(), 60)
        if minutes[0] == 2 :
            return 2
    
        
def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel


def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)
    GPIO.output(L5, state)

# def checkSpecialKeys():
#     global input
#     pressed = False

#     # GPIO.output(L5, GPIO.HIGH)

#     # if (GPIO.input(C1) == 1):
#     #     print("Input reset!");
#     #     pressed = True

#     GPIO.output(L5, GPIO.LOW)

#     # global flag
#     # # print(len(input))
#     # if len(input) > flag :
#     #     flag = len(input)
#     print("conut :",len(input))

#     if pressed:
#         input = ""

#     return pressed


def readLine(line, characters,row):
    global input

    # detect button presses
    GPIO.output(line, GPIO.HIGH)
    
      
    if row == "row1" : # Row 1 : 7 8 9
        if(GPIO.input(C1) == 1): input = input + characters[0] # : 7
        if(GPIO.input(C4) == 1): input = input + characters[1] # : 8
        if(GPIO.input(C3) == 1): input = input + characters[2] # : 9
        
    elif row == "row2" : # Row 2 : 4 5 6
        if(GPIO.input(C1) == 1): input = input + characters[0] # : 4
        if(GPIO.input(C2) == 1): input = input + characters[1] # : 5
        if(GPIO.input(C3) == 1): input = input + characters[2] # : 6
        
    elif row == "row3" : # Row 3 : 1 2 3
        if(GPIO.input(C1) == 1): input = input + characters[0] # : 1
        if(GPIO.input(C2) == 1): input = input + characters[1] # : 2
        if(GPIO.input(C3) == 1): input = input + characters[2] # : 3
    
    elif row == "row4" : # Row 3 : 0
        if(GPIO.input(C4) == 1): input = input + characters[0] # : 0
        
    else: # Row 4 : * #
        if(GPIO.input(C1) == 1): input = input + characters[0] # : *
        if(GPIO.input(C3) == 1): input = input + characters[1] # : #
        
        
    GPIO.output(line, GPIO.LOW)

def matrix_keypad(start):
    
    global input
    input = ""
    
    global L1,L2,L3,L4,L5
    L1 = 21
    L2 = 26
    L3 = 13
    L4 = 5
    L5 = 6

    # These are the four columns
    global C1,C2,C3,C4
    C1 = 12
    C2 = 19
    C3 = 20
    C4 = 16



    # The GPIO pin of the column of the key that is currently
    # being held down or -1 if no key is pressed
    global keypadPressed
    keypadPressed = -1



    # Setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)
    GPIO.setup(L5, GPIO.OUT)

    # Use the internal pull-down resistors
    GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
    # GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
    # GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
    # GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)
    
    # try:
        
    while True:
        # # If a button was previously pressed,
        # # check, whether the user has released it yet
        # if keypadPressed != -1:
        #     setAllLines(GPIO.HIGH)
        #     if GPIO.input(keypadPressed) == 0:
        #         keypadPressed = -1
        #     else:
        #         time.sleep(0.2)
        # # just read the input
        # else:
        cal = datetime.now() - start
        # print(cal)
        minutes = divmod(cal.total_seconds(), 60)
        if minutes[0] == 2 :
            return "time_out"
        
        readLine(L1, ["7","8","9"],"row1")
        readLine(L2, ["4","5","6","B"],"row2")
        readLine(L3, ["1","2","3"],"row3")
        readLine(L4, ["0"],"row4")
        readLine(L5, ["*","#"],"row5")
        if len(input) > 0 :
            return input
        # time.sleep(0.2)
                
    # except KeyboardInterrupt:
    #     print("\nApplication stopped!")
        
# print("test")
# print(matrix_keypad(datetime.now()))