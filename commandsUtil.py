import random # Used for humanization
import time # Used for waiting
import pyautogui

def randomOffset(max=100):
    return random.randrange(-max,max)

def randomRange(min=0,max=100):
    return random.randrange(min,max)

def randomSeconds(minMs=0,maxMs=1000):
    # Takes in MS values and returns a random time in seconds. Used for timers.
    return random.randrange(minMs,maxMs)*0.001

def isHuman(state):
    return state["human"]

def waitIfHuman(state):
    # Waits a small amount of random time
    if state["human"]:
        seconds = random.randrange(15,50)*0.001
        time.sleep(seconds)

def safeInt(str):
    # Sometimes string do not convert to ints correctly
    # This gives a user-friendly error message when this happens
    try:
        res = int(str)
        return res
    except:
        print('Cannot convert: '+str+' to int!')
        quit()
        return False

def safeFloat(str):
    # Sometimes string do not convert to floats correctly
    # This gives a user-friendly error message when this happens
    try:
        res = float(str)
        return res
    except:
        print('Cannot convert: '+str+' to float!')
        quit()
        return False

def getXY(arg):
    # Splits an arg into X and Y integer values
    argSplit = arg.split(',')
    x = int(argSplit[0])
    y = int(argSplit[1])
    return [x,y]

def getAB(arg):
    # Splits an arg into A and B string values
    argSplit = arg.split(',')
    a = argSplit[0]
    b = argSplit[1]
    return [a,b]

def defaultArg(arg, default):
    # Replaces an empty arg value ("NA") with a default argument
    # If the arg does not have an empty ("NA") value, we return the original arg
    if arg == "NA":
        return default
    return arg

def requireArg(arg):
    # Requires that user supplies an arg for this command
    # If no arg is supplied the script will quit
    if arg == "NA":
        print('ERROR: This command requires an argument!')
        quit()

def verifyKey(arg):
    # Verifies that the key the user supplied is a valid key
    # If its not the script will quit
    foundKey = False
    for key in pyautogui.KEY_NAMES:
        if key == arg:
            foundKey = True
    if foundKey == False:
        print('ERROR: Cant find a key to press with name: '+arg)
        print('Available Names: ')
        print(pyautogui.KEY_NAMES)
        quit()
    return True