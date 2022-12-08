#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
screenX, screenY = pyautogui.size()
print('Screen Resolution: ')
print(str(screenX)+'x'+str(screenY))
print('Current Mouse Position: ')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')