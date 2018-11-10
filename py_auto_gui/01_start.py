import pyautogui
current = pyautogui.position()
print(current)

#762, 872
x = current[0]
y = current[1]
print(x)
pyautogui.moveTo(771, 872, duration=1)
# pyautogui.click(x=771, y=872, clicks=1, interval=1, button='left')
pyautogui.typewrite('Hello world!\n', interval=1)