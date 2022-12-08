# Cory (Scriptable Python Based GUI Bot) 
Cory is a python based interpreter for a very simple yet flexible GUI automation scripting language (CoryScript). 

![cory](https://static1.personality-database.com/profile_images/55516dd0a3aa4ea198702184b28b22af.png)

The CoryScript scripting language is very human readable and looks something like SQL. A command to move the mouse to a given position is like this:

```
GOTO 100,200
```

This will move the mouse to the screen coordinates x=100, y=200.

The goal of Cory is to to decrease the cognitive load and onboarding required to write simple GUI automation scripts. In theory, just about anyone with basic computer knowledge should be able to create a bot with CoryScript. 

The secondary goal of Cory is to provide "free" humanization to your automation scripts. Cory makes it easy to ensure that the bots your create will appear like human users to anyone monitoring the app/website that it is used on. This happens by injecting small amount of randomization into the actions preformed. 

# Running a CoryScript (Setup)
Before you can use Cory, you need to ensure you have Python3 installed then you need to install the Python dependencies:

```
pip install -r requirements.txt
```

```
python cory.py someScript.txt
```

# Running Example Scripts
There are several example scripts in the `/examples` directory. You can run them like this:
```
python cory.py examples/someExample.txt
```

For instance, to run the alert example do:
```
python cory.py examples/alert.txt
```

# Human Mode
Cory comes with "free humanization". All you need to do to enable it is type `human` at the end of your launch command. 

```
python cory.py someScript.txt human
```

When the `human` flag is added, Cory will automatically do it's best to act like a human. This means adding a little bit or randomization and delay here and there. This won't be enough to trick other actual humans, but it should be enough to get around basic anti-bot detection tools. Essentially it makes it less obvious that Cory is a bot at the expense of your scripts running a little slower. 

# CoryScript Syntax
CoryScript has a very simple syntax. Each line of a script file must contain exactly one command. 

Any empty line will result in a syntax error. Each line must contain a command

A command can have anywhere between 0 and 2 arguments supplied

```
COMMAND ARGUMENT1,ARGUMENT2
```


**NOTE: Tying the commands in uppercase is not required but it is recommended.** 

Some commands have a default argument. If you are using a command with a default argument, you can omit the argument from the line.

Some commands require and argument (no default). If you are using a command that requires an argument and you do not supply one, the script will quit on that line. 

A simple CoryScript might look like this:
```
ALERT Running a new script!
GOTO 100, 100
WAIT 2
CLICK 
```

This script will show an alert box with the text "Running a new script!". Once the user clicks "OK" the mouse will be moved to 100, 100. Then the script will wait for 2 seconds and send a mouse click to the current mouse location.

Cory features basic runtime error handling for CoryScript. If your script contains a syntax error, the script will run up until that point and then quit with an error message shown in your command line output. 

CoryScript also supports comments. These follow python `#` syntax. 

```
# This is a comment
GOTO 100,100
```

# Cory Utility (Script Helper Tool)
When writing CoryScripts, you will often need to know your current screen resolution and mouse position.

To make this easier, there is a python script called `/util.py` that contains a simple helper tool to provide this info.

Run the utility:
```
python util.py
```

# CoryScript Commands
## Cheat Sheet
```
EXPECT <X>,<Y>
GOTO <X>,<Y>
CLICK <N=1>
WAIT <N=1>
HOTKEy <KEY1>,<KEY2>
NEWLINE <N=1>
SELECTALL
FULLSCREEN
ALERT <ALERT TEXT>
CONFIRM <CONFIRM TEXT>
DEBUG <DEBUG TEXT>
PYTHON <SOME PYTHON>
PYTHONFILE <SOMEFILE>
LOOP <TAG>
PRESS <KEY>
```

## EXPECT
```
EXPECT 640,480
EXPECT <X>,<Y>
```
Expects the screen size match the given values. If the screen size does not match the script will quit. This is useful for ensuring that the GOTO coordinates you enter will be accurate. 

X = Screen X resolution

Y = Screen Y resolution

## GOTO
```
GOTO <X>,<Y>
```
Moves the mouse to the given coordinates.

X = X Position

Y = Y Position

**NOTE: In computer software, the origin (0,0) is the top left corner of your screen. This is opposed to traditional graphing math, where the origin is the bottom left.**

```
 0 1 2 3 . . .
0
1
2
3
.
.
.
```
## SCROLL
```
SCROLL
SCROLL <N=1>
```
Scrolls the active window up or down by N scroll "clicks". This behavior will vary on each OS. A negative value scrolls down and positive scrolls up. 

N = Amount of scroll "clicks". (Default = 1)
## CLICK
```
CLICK
CLICK <N=1>
```
Sends a left mouse click at the current mouse position. 

N = Amount of times to click. (Default = 1)
## WAIT
```
WAIT
WAIT <N=1>
```
Waits for N seconds.

N = Seconds to wait. (Default = 1)
## WRITE
```
WRITE <SOME TEXT>
WRITE Hello World
```
Types out the given text. Make sure you have your text box selected with CLICK before typing
## WRITEFILE
```
WRITEFILE <SOMEFILE>
WRITEFILE some_text_file.txt
```
Reads a file and types out the given text. Make sure you have your text box selected with CLICK before typing
## HOTKEY
```
HOTKEY <KEY1>,<KEY2>
HOTKEY ctrl,a
```
Presses the given key combination. 

KEY1 = First key top press and hold

KEY2 = Second key to press

## NEWLINE
```
NEWLINE <N=1>
```
Creates a new line in the current text field (shift+enter).

N = Number of new lines. (Default = 1)
## SELECTALL
```
SELECTALL
```
Selects all of the text currently available (ctrl+a).
## FULLSCREEN
```
FULLSCREEN
```
Puts the active window into full screen mode if possible (f11).
## ALERT
```
ALERT <Some Alert Message>
```
Shows an alert message popup window on the screen with the given text. 

Waits for the user to press "OK" before the script continues.
## CONFIRM
```
CONFIRM <Some Confirm Message>
```
Shows an confirm message popup window on the screen with the given text. 

If the user presses "OK" the script will continue. If they press "Cancel" the script will exit. 
## DEBUG
```
DEBUG <Some DEBUG Message>
```
Prints the given message to the command line.

Does not wait for the user to accept. 
## PYTHON
```
PYTHON <SOME PYTHON CODE>
PYTHON sum([1,2,3,4])
```
Executes the given Python code.

**NOTE: Use with caution!**
## PYTHONFILE
```
PYTHON <SOMEFILE>
PYTHON someFile.py
```
Executes the given Python file.

**NOTE: Use with caution!**
## LOOP (DECLARE)
```
LOOP <TAG=Null>
LOOP SomeTag
```
Sets up a loop with the given tag

TAG = The name of the loop. Omit for simple looping.
## LOOP (USE)
```
LOOP <TAG=Null> <ITERATIONS=Infinity>
LOOP SomeTag 3
```
Runs up a loop with the given tag

TAG = The name of the loop. Omit for simple looping.

ITERATIONS = The amount of times to run the loop. Not possible with simple looping.
## PRESS
```
PRESS <KEY>
PRESS esc
```
Presses the given key. 

KEY  = Key to press

-------

# Available Keys
This is a list of acceptable inputs for the HOTKEY and PRESS commands
```
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```

# Looping
Looping is one of the more advanced features of Cory. The `LOOP` command lets you run the same chunk of the script multiple times. This can keep you from needing to type out the same series of commands over and over, and can be used to create an infinite automation loop. 

## Simple Looping

The simplest way to get started with using loops is to put just put one `LOOP` command where you want to start the loop, and another `LOOP` command where you want to end it:
```
ALERT We are going to enter a loop now!
LOOP
CONFIRM We are in the loop! Press "cancel" to exit.
LOOP
```

This will show the confirmation bot over and over until you press "cancel".

**NOTE: Simple looping will always run forever. To cancel your current script, press ctrl+c on the command line!**

## Advanced Looping

Advanced looping allows you to use multiple loops in the same script and set how many times you want each loop to run.

To get started with more advanced loop usage, you first need to declare a "loop point". To declare a loop point, we use the `LOOP` command followed by a unique string (the "tag"). 

```
LOOP SomeLoopTag
```

You can think of a loop point as a kind of bookmark within your script. Once we have declared a loop point, we can make our script return to that point whenever we want.

In the context of an actual script, it might look something like this:
```
ALERT Starting a loop demo
LOOP SomeLoopTag
CONFIRM We are in the loop! Press "cancel" to exit.
```
So now that we set up our loop point with the tag "SomeLoopTag" we can return to it:

```
ALERT Starting a loop demo
LOOP SomeLoopTag
CONFIRM We are in the loop! Press "cancel" to exit.
# Return to the second line and keep going
LOOP SomeLoopTag
```

If we run this script we will get an infinite series of confirmation windows. 

Notice that the second time we used the `LOOP` command it looked exactly the same. Once a loop point has been declared, any subsequent uses of the `LOOP` command using this same tag will *call the loop* instead of declaring it. By default, calling a loop command without a number after it will run the loop forever. If we want to run it some specific amount of times instead, we can do that like this:

```
ALERT Starting a loop demo
LOOP SomeLoopTag
CONFIRM We are in the loop! Press "cancel" to exit.
# Return to the second line and keep going
LOOP SomeLoopTag 123
```

The above script will run the loop 123 times. 

Since each loop point has a unique tag assigned, we can have as many loop points as we want:

```
ALERT Starting a loop demo
LOOP SomeLoopTag
CONFIRM We are in the first loop! Press "cancel" to exit.
# Return to the second line and keep going
LOOP SomeLoopTag 3
LOOP SomeOtherLoopTag
CONFIRM We are in the second loop! Press "cancel" to exit.
# Return to the second line and keep going
LOOP SomeOtherLoopTag 3
```

**NOTE: Make sure you give your first loop an iteration count (number) or you will never reach the second loop!**

## Super Advanced Looping

You can even nest loops within one another:
```
# Declare the loop
LOOP Main
CONFIRM This is the main loop. Press Cancel to exit.
LOOP Sub
CONFIRM This is a sub loop. Press Cancel to exit.
# Call the sub-loop
LOOP Sub 3
LOOP Sub2
CONFIRM This is the second sub loop. Press Cancel to exit.
# Call the second sub-loop
LOOP Sub2 3
# Call the loop
LOOP Main 2
```

# How Does It Work?
Cory is essentially a wrapper for the PyAutoGUI module. It works by reading a script file and breaking that file into new lines. 

Each line is then broken into a command and argument. 

Using the commands `listing` dictionary created in `/commands.py`, Cory checks to see if the current line represents a valid command. 

If it does it will execute that command (usually a wrapper for some PyAutoGUI calls) and move on to the next line. 

The logic for reading and parsing the scripts is in `/cory.py`. The logic for each available command (as well as the definition of the commands listing dictionary) is in `/commands.py`. 

-------

## Freeze Requirements
`pip freeze > requirements.txt`

## Install Requirements
`pip install -r requirements.txt`
