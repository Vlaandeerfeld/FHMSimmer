import pyautogui
import time

list1 = ['calgaryflames', 'arizonacoyotes', 'tofinocowabungas']

time.sleep(10)

def simToNextDay(): 
    selectManager('Bettman')
    time.sleep(1)
    pyautogui.click(779, 20)#play
    time.sleep(1)
    pyautogui.click(832, 148)#simtonextday
    time.sleep(3)
    pyautogui.screenshot('upload.png')
def simDay():
    list2 = []
    selectManager('Bettman')
    time.sleep(1)
    for p in list1:
        z = 'anything'
        try:
            x, y = pyautogui.locateCenterOnScreen(p + '.png', confidence = 0.8)
            z = "something"
        except:
            gotoSchedule()
            z = "nothing"
            print(z)
        
        if z == "something":
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('sim.png', region=(x, y, 300, 100))
            pyautogui.click(x, y)
            time.sleep(1)
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

def gotoPreviousDay():
    pyautogui.click(1278, 255)
    
def saveFile():
    pyautogui.click(196, 18)
    time.sleep(3)
    pyautogui.click(221, 51)

def uploadFile():    
    selectManager('Bettman')
    time.sleep(1)
    pyautogui.click(196, 18)
    time.sleep(3)
    pyautogui.click(212, 182)
    time.sleep(3)
    pyautogui.click(422, 182)
    time.sleep(3)
    pyautogui.click(1087, 385)
    time.sleep(1)
    pyautogui.screenshot('upload.png')
    time.sleep(1)

def selectManager(manager):
    pyautogui.click(436, 18)
    time.sleep(1)
    pyautogui.click(417, 285)
    time.sleep(3)
        
    if manager == 'Young':
        x, y = pyautogui.locateCenterOnScreen('Young.png')
        pyautogui.click(x, y)
    elif manager == 'Blaschke':
        x, y = pyautogui.locateCenterOnScreen('Blaschke.png')
        pyautogui.click(x, y)
    elif manager == 'Liszewski':
        x, y = pyautogui.locateCenterOnScreen('Liszewski.png')
        pyautogui.click(x, y)
    elif manager == 'Bettman':
        x, y = pyautogui.locateCenterOnScreen('Bettman.png')
        pyautogui.click(x, y)    

    pyautogui.click(974, 810)

def pictureRoster(manager):
    gotoRoster(manager)
    time.sleep(1)
    pyautogui.screenshot('roster' + manager + '.png')
    time.sleep(1)
    gotoInjuryList()
    time.sleep(1)
    pyautogui.screenshot('injurylist' + manager + '.png')
    time.sleep(1)
    gotoDepthCharts()
    time.sleep(1)
    pyautogui.screenshot('depthcharts' + manager + '.png')
    
def gotoDepthCharts():
    pyautogui.click(475, 184)
    
def gotoInjuryList():
    pyautogui.click(659, 219)

def gotoRoster(manager):
    selectManager(manager)
    
def goto5on5():
    pyautogui.click(151, 185)
    
def gotoPowerplay():
    pyautogui.click(268, 223)
    
def gotoPenaltykill():
    pyautogui.click(451, 223)

def goto3on3():
    pyautogui.click(635, 223)
  
def gotoGoalieStarts():
    pyautogui.click(804, 223)

def gotoTactics():
    pyautogui.click(349, 184)

def gotoFinances():
    pyautogui.click(1033, 184)
    
def gotoTraining():
    pyautogui.click(1349, 180)
    
def pictureLines(manager):
    selectManager(manager)
    time.sleep(1)
    goto5on5()
    time.sleep(1)
    pyautogui.screenshot('5on5' + manager + '.png')    
    time.sleep(1)
    gotoPowerplay()
    time.sleep(1)
    pyautogui.screenshot('powerplay' + manager + '.png')    
    time.sleep(1)
    gotoPenaltykill()    
    time.sleep(1)
    pyautogui.screenshot('penaltykill' + manager + '.png')
    time.sleep(1)
    goto3on3()
    time.sleep(1)
    pyautogui.screenshot('3on3' + manager + '.png')    
    time.sleep(1)
    gotoGoalieStarts()
    time.sleep(1)
    pyautogui.screenshot('goaliestarts' + manager + '.png')

def pictureTactics(manager):
    selectManager(manager)
    time.sleep(1)
    gotoTactics()
    time.sleep(1)
    pyautogui.screenshot('global1' + manager + '.png')
    time.sleep(1)
    pyautogui.click(x=1162, y=625)
    pyautogui.scroll(-750)
    time.sleep(1)
    pyautogui.screenshot('global2' + manager + '.png')
    time.sleep(1)
    pyautogui.scroll(-1500)
    time.sleep(1)
    pyautogui.screenshot('global3' + manager + '.png')
    
def pictureFirstMonth(manager):
    selectManager(manager)
    time.sleep(1)
    gotoFinances()
    time.sleep(1)
    pyautogui.screenshot('finances' + manager + '.png')
    time.sleep(1)
    gotoTraining()
    time.sleep(1)
    pyautogui.screenshot('training' + manager + '.png')    

def pictureLastDay():
    selectManager('Bettman')
    time.sleep(1)
    gotoSchedule()
    time.sleep(1)
    gotoPreviousDay()
    time.sleep(1)
    pyautogui.screenshot('previousday.png')
    
def importFiles():
    selectManager('Bettman')
    time.sleep(1)
    pyautogui.click(196, 18)
    time.sleep(1)
    pyautogui.click(212, 182)
    time.sleep(3)
    pyautogui.click(422, 182)
    time.sleep(3)
    pyautogui.click(1065, 315)
    
def exitSave():
    selectManager('Bettman')
    time.sleep(1)
    pyautogui.click(196, 18)
    time.sleep(1)
    pyautogui.click(193, 206)
    time.sleep(1)
    pyautogui.click(996, 611)
    time.sleep(20)
    
def launchFHM():
    pyautogui.click(384, 426)
    time.sleep(10)
    pyautogui.click(975, 442)
    time.sleep(1)
    pyautogui.click(853, 275)
    time.sleep(1)
    pyautogui.click(1144, 878)
    time.sleep(25)
    x, y = pyautogui.locateCenterOnScreen('Bettman.png')
    pyautogui.click(x, y) 
    time.sleep(2)
    pyautogui.click(1103, 810)


print(pyautogui.position())
