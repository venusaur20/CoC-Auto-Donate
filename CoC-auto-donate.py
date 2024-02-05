import pyautogui, time, keyboard

######################################################## Gets Mouse Pos
#while True:
#    currentMouseX, currentMouseY = pyautogui.position()
#    print(currentMouseX, currentMouseY)
#    
#    if keyboard.is_pressed("q"):
#        break
 
#    time.sleep(1)

time.sleep(2)
pyautogui.click(18, 470)


while True:
     troop = pyautogui.locateOnScreen(r'C:\Users\Hasan\Documents\GitHub-Hasan\CoC-Auto-Donate\CoC Troops\Barbarian Request.PNG', confidence = 0.9, grayscale = False, region = (3, 108, 582, 945))
 
     pyautogui.leftClick(600, 488)
     pyautogui.leftClick(70, 815)
     pyautogui.leftClick(621, 173)
     
#     if troop == "barbarian":
     pyautogui.leftClick(334, 618)
     
    
     if keyboard.is_pressed("q"):
         break