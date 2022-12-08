import pyautogui
import sys
import commands
import commandsUtil

state = {
    "scriptLocation": "SCRIPT.txt",
    "script":"",
    "human":False,
    "curLine":0,
    "loops": []
}

def readScript():
    try:
        f = open(state['scriptLocation'], "r")
    except:
        print('ERROR: CANT OPEN SCRIPT: '+state['scriptLocation'])
        quit()
    content = f.read()
    state["script"] = content

def executeScript():
    # Split the script into lines
    lines = state["script"].split('\n')
    if(state["human"]):
        print('Running in Human mode!')
    # Go through each line of the script
    while state['curLine'] < len(lines):
        line = lines[state['curLine']]
        print(str(state['curLine'])+': '+line)
        # We need to extract the command and the arg from the line
        cmd = 'NA' # Placeholder value
        arg = 'NA' # Placeholder value
        # Split the line into the command and the argument
        split = line.split(' ')
        # Get the command
        cmd = split[0]
        # Check for empty lines
        if len(line) == 0:
            nextLine()
            continue # Move to the next line of the script
        if line[0]==" ":
            nextLine()
            continue # Move to the next line of the script
        # Check for comments
        if line[0]=="#":
            # This line is a comment
            nextLine()
            continue # Move to the next line of the script
        # Make sure the command is in uppercase
        cmd = cmd.upper()
        # Only some commands take an argument
        if len(split) > 1: # Check to see if we have an argument
            # Get the arg
            arg = split[1:]
            arg = ' '.join(arg)
        # Check if we have a loop command
        if handleLoops(cmd, arg):
            continue # Return to start of while loop
        # Check that we have a valid command
        foundCmd = False
        for availableCmd in commands.listing:
            if availableCmd == cmd:
                foundCmd = True
        if foundCmd:
            res = commands.listing[cmd](arg, state)
            if(res != True):
                print('ERROR: THERE WAS A PROBLEM WITH YOUR LAST '+cmd+' COMMAND AT LINE '+str(state['curLine']))
                print('READ: '+line)
                return # Quit
        else:
            print('ERROR: UNKNOWN COMMAND '+cmd+' AT LINE '+str(state['curLine']))
            return # Quit
        # Move to next line
        nextLine()
    print('SCRIPT COMPLETE!')

def handleLoops(cmd, arg):
    if cmd != 'LOOP':
        # This was not a loop command
        return False
    argSplit = arg.split(' ')
    loopTag = argSplit[0].lower()
    loopCount = 0
    argHasCount = len(argSplit) > 1
    if argHasCount:
        loopCount = commandsUtil.safeInt(argSplit[1])
    # Check if the loop exists already
    foundLoop = {}
    for loop in state['loops']:
        matchTag = loop['tag'] == loopTag
        if matchTag: # found
            foundLoop = loop
            break
    if foundLoop != {} and argHasCount: 
        print('FOUND EXISTING LOOP: '+loopTag)
        # Set the line number to the desired loop point
        if foundLoop['count'] == -1:
            # This is the first time hitting this loop
            # Set the loop count
            foundLoop['count'] = loopCount-1
            if foundLoop['count'] > 0:
                # Set our current line to the loop point
                state['curLine'] = foundLoop['line']
                foundLoop['count'] = foundLoop['count'] -1
                # Loop to loop point
                print('START LOOPING: '+foundLoop['tag']+' ('+str(foundLoop['count'])+')')
                return True  # return to start of while loop
            else:
                # Edge case
                # We dont actually loop because it was set to one
                print('LOOP END: '+foundLoop['tag'])
                foundLoop['count'] = 0
                nextLine()
                return True  # return to start of while loop
        elif foundLoop['count'] > 0:
            # Loop back to the loop point
            state['curLine'] = foundLoop['line']
            # Remove one from loop count
            foundLoop['count'] = foundLoop['count'] -1
            print('LOOPING: '+foundLoop['tag']+' ('+str(foundLoop['count'])+')')
            return True  # return to start of while loop
        else:
            # The loop has come to an end (no more count)
            foundLoop['count'] = -1 # Reset loop
            print('LOOP END: '+foundLoop['tag'])
            nextLine()
            return True  # return to start of while loop
    elif foundLoop != {}:
        print('FOUND EXISTING LOOP: '+loopTag+ ' WITH EMPTY COUNT')
        state['curLine'] = foundLoop['line']
        print('START LOOPING: '+foundLoop['tag']+' (INFINITE)')
    if foundLoop == {}:
        # Loop doest exist so append it
        state['loops'].append({'tag':loopTag, 'line':state['curLine'], 'count':-1})
        print('CREATED NEW LOOP: '+loopTag)
    nextLine()
    return True # return to start of while loop

def nextLine():
    state['curLine'] = state['curLine']+1

def setup():
    if len(sys.argv) > 1 :
        state["scriptLocation"] = sys.argv[1]
    if len(sys.argv) > 2 :
        if sys.argv[2].lower() == 'human':
            state["human"] = True
    readScript()
    executeScript()
setup()
