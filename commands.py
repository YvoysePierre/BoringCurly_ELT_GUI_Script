import pyautogui
import time # Used for waiting
import os # Used for executing system commands
import subprocess # Used for executing system commands as a subprocess
import commandsUtil # command utilities

def expect(arg, state):
    # Expect a specific screen resolution
    # Return error if expectation is not met
    commandsUtil.requireArg(arg)
    screenX, screenY = pyautogui.size()
    expectX, expectY = commandsUtil.getXY(arg)
    passed = True
    if screenX != expectX:
        passed = False
    if screenY != expectY:
        passed = False
    if passed == False:
        alertText = 'Expected: '+str(expectX)+'x'+str(expectY)+'. Got: '+str(screenX)+'x'+str(screenY)
        pyautogui.alert(text=alertText, title='SCREEN RESOLUTION ISSUE', button='OK')
        return 0
    return 1

def goto(arg, state):
    # Move the mouse to the given coords
    commandsUtil.requireArg(arg)
    x, y = commandsUtil.getXY(arg)
    # If we are pretending to be human, emulate human mouse movement
    if(commandsUtil.isHuman(state)):
        # Create and initial mouse movement to emulate someone grabbing the mouse
        startingOffsetX = commandsUtil.randomOffset(100)
        startingOffsetY = commandsUtil.randomOffset(100)
        moveTime = commandsUtil.randomSeconds(25,100)
        pyautogui.move(startingOffsetX,startingOffsetY, moveTime)
        # Move the mouse in randomized chunks towards the target
        chunks = 3
        for chunk in range(chunks):
            # Get the current mouse position
            curX, curY = pyautogui.position()
            # Calculate the difference between the current location and the destination
            diffX = x - curX
            diffY = y - curY
            if diffX == 0 and diffY == 0:
                # We reached the target
                return 1
            # Get our current chunk number
            # Used to divide the difference into our next target
            chunkNum = chunks - chunk
            # Build our random offset
            offsetX = 0
            offsetY = 0
            if(chunk < chunks-1):# Dont randomize the last chunk
                offsetX = commandsUtil.randomOffset(300)
                offsetY = commandsUtil.randomOffset(300)
            # Generate the next target
            targetX = (diffX/chunkNum)+offsetX
            targetY = (diffY/chunkNum)+offsetY
            # Move to the next target over a random amount ms between 250 and 1000
            moveTime = commandsUtil.randomSeconds(250,1000)
            pyautogui.move(targetX,targetY, moveTime)
    else:
        pyautogui.moveTo(x, y, 0.2)
    return 1

def scroll(arg, state):
    # Scrolls the given amount of pixels
    commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeInt(arg)
    if commandsUtil.isHuman(state):
        direction = 1 if arg > 0 else -1
        count = round(arg / 10)
        for i in range(count):
            pyautogui.scroll(direction*10)
        return 1
    pyautogui.scroll(arg)
    return 1

def click(arg, state):
    # Send a click at the current mouse position
    # The value of arg determines the amount of clicks
    arg = commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeInt(arg)
    for i in range(arg):
        commandsUtil.waitIfHuman(state)
        pyautogui.click() 
    return 1

def wait(arg, state):
    # Wait for the given amount of time in seconds
    arg = commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeFloat(arg)
    if(commandsUtil.isHuman(state)):
        arg = arg + commandsUtil.randomSeconds(500,1000)
    time.sleep(arg)
    return 1

def write(arg, state):
    # Type of the given string of text
    # Can not handle new lines
    commandsUtil.requireArg(arg)
    argSplit = [*arg] #Split the string into an array of single chars
    for char in argSplit:
        commandsUtil.waitIfHuman(state)
        pyautogui.write(char)
    return 1

def writeFile(arg, state):
    try:
        f = open(arg, "r")
    except:
        print('ERROR: CANT OPEN FILE: '+arg)
        return 0
    content = f.read()
    write(content, state)
    return 1

def hotkey(arg, state):
    commandsUtil.requireArg(arg)
    arg = arg.lower() # All key names are lowercase
    key1, key2 = _getAB(arg)
    commandsUtil.verifyKey(key1)
    commandsUtil.verifyKey(key2)
    commandsUtil.waitIfHuman(state)
    pyautogui.hotkey(key1, key2)
    return 1

def newLine(arg, state):
    arg = commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeInt(arg)
    for i in range(arg):
        commandsUtil.waitIfHuman(state)
        pyautogui.hotkey('shift', 'enter')
    return 1

def selectAll(arg, state):
    commandsUtil.waitIfHuman(state)
    pyautogui.hotkey('ctrl', 'a')
    return 1

def fullScreen(arg, state):
    commandsUtil.waitIfHuman(state)
    pyautogui.press('f11')
    return 1

def alert(arg, state):
    pyautogui.alert(text=arg, title='ALERT', button='OK')
    return 1

def confirm(arg, state):
    res = pyautogui.confirm(text=arg, title='CONFIRM', buttons=['OK', 'Cancel'])
    if(res == 'Cancel'):
        print('The user ended the script!')
        quit()
    return 1

def debug(arg, state):
    print('DEBUG: '+arg)
    return 1

def python(arg, state):
    res = eval(arg)
    print('RES: '+str(res))
    return 1

def pythonFile(arg, state):
    try:
        f = open(arg, "r")
    except:
        print('ERROR: CANT OPEN FILE: '+arg)
        return 0
    content = f.read()
    exec(content)
    return 1


def execute(arg, state):
    commandsUtil.requireArg(arg)
    os.system(arg)
    return 1

def executeSub(arg, state):
    commandsUtil.requireArg(arg)
    subprocess.Popen([arg])
    return 1

def press(arg, state):
    # Press the given key
    commandsUtil.requireArg(arg)
    arg = arg.lower() # All key names are lowercase
    commandsUtil.verifyKey(arg)
    commandsUtil.waitIfHuman(state)
    pyautogui.press(arg)
    return 1




listing = {
    "EXPECT": expect,
    "GOTO": goto,
    "SCROLL": scroll,
    "CLICK": click,
    "WAIT": wait,
    "WRITE": write,
    "WRITEFILE": writeFile,
    "HOTKEY": hotkey,
    "NEWLINE": newLine,
    "SELECTALL": selectAll,
    "FULLSCREEN": fullScreen,
    "ALERT": alert,
    "CONFIRM": confirm,
    "DEBUG": debug,
    "PYTHON": python,
    "PYTHONFILE": pythonFile,
    "EXECUTE": execute,
    "EXECUTESUB": executeSub,
    "PRESS": press
}