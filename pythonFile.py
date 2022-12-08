import pyautogui
print("Running some manually created Python code")
pyautogui.alert(text='Moving to 100,100', title='ALERT', button='OK')
pyautogui.moveTo(100, 100, 1)