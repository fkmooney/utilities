import pyautogui

# set a puase between each step (to allow for programs to keep up or for you to take control)
pyautogui.PAUSE = .2

# Moving the cursor to the upper-left corner of the screen will raise an exception and stop process
pyautogui.FAILSAFE = True

# to type keyboard shortcuts
pyautogui.keyDown('alt')
pyautogui.press('tab') # up and down
pyautogui.keyUp('alt')

# another way to type keyboard shortcut, doesn't work for alt-tab
pyautogui.hotkey('ctrl', 'n')

# enter key presses
pyautogui.typewrite('kempton.mooney@npd.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('Subject Text')
pyautogui.press('tab')
pyautogui.typewrite('Body of email')

pyautogui.hotkey('altleft', 's')


"""
######## Additional Commands #########
# get size of screen so you have dimensions
print(pyautogui.size())
width, height = pyautogui.size()

# click mouse at certain position
pyautogui.click(100, 150, button='left')


pyautogui.doubleClick()

# get screen shot
image = pyautogui.screenshot()
image.save("screenshot.png")

time.sleep(5)

# get mouse current position
print(pyautogui.position())

# movescursor
pyautogui.moveTo(100, 100, duration=0.25)

pyautogui.keyDown('k')
pyautogui.keyUp('k')
"""
######################################
