import pyautogui
screenWidth,screenHeight = pyautogui.size() # width and height
print(screenWidth,screenHeight)
currentMouseX,currentMouseY = pyautogui.position() # current position of mouse
print(currentMouseX,currentMouseY)