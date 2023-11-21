import pyautogui
import time

list1 = ['calgaryflames', 'arizonacoyotes', 'tofinocowabungas']

time.sleep(10)

def simToNextDay(): 
    pyautogui.click(779, 20)#play
    time.sleep(5)
    pyautogui.click(832, 148)#simtonextday
    time.sleep(3)
    pyautogui.screenshot('upload.png')
def simDay():
    list2 = []
    for p in list1:
        try:
            x, y = pyautogui.locateCenterOnScreen(p + '.png')
            z = "something"
        except:
            gotoSchedule()
            z = "nothing"
            print(z)
        
        if z == "something":
            time.sleep(3)
            x, y = pyautogui.locateCenterOnScreen('sim.png', region=(x, y, 300, 100))
            pyautogui.click(x, y)
            time.sleep(5)
            x, y = pyautogui.locateCenterOnScreen('report.png', region=(x, y - 50, 200, 100))
            pyautogui.click(x, y)
            time.sleep(1)
            pyautogui.screenshot('upload1' + p + '.png')
            time.sleep(1)
            pyautogui.scroll(-1500)
            time.sleep(1)
            pyautogui.screenshot('upload2' + p + '.png')
            time.sleep(1)
            pyautogui.scroll(-1500)
            time.sleep(1)
            pyautogui.screenshot('upload3' + p + '.png')
            time.sleep(1)
            pyautogui.scroll(-1500)
            time.sleep(1)
            pyautogui.screenshot('upload4' + p + '.png')
            gotoSchedule()
            list2.append(p)
    return(list2)
           
def gotoSchedule():
    pyautogui.click(535, 17)
    time.sleep(3)
    pyautogui.click(624, 106)

def saveFile():
    pyautogui.click(196, 18)
    time.sleep(3)
    pyautogui.click(221, 51)

def uploadFile():
    pyautogui.click(196, 18)
    time.sleep(3)
    pyautogui.click(212, 182)
    time.sleep(3)
    pyautogui.click(422, 182)
    time.sleep(3)
    pyautogui.click(1087, 385)
    
print(pyautogui.position())
