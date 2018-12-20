####Environment Setting
###pip install pyautogui
import pyautogui, sys
import random
import time
mouse = pyautogui

print("Toulove WaiGua by RedHerrings.\n")
totalworks = int(input("Please specify how many rounds you would like to play:"))
print("Going to play " + str(totalworks) + " rounds.\n")
print("Please minimize the python window and go to 本丸 now. \nToulove Waigua will start in 10 seconds.")
time.sleep(10)

CoordinateSelect=0
n=0  #nth coordinate
x=[]  #vector of x
y=[]  #vector of y
term=[]
totaltime=[]

x.append(int(820))  #x coordinate
y.append(int(520))  #y coordinate
x.append(int(820))  #x coordinate
y.append(int(400))  #y coordinate

def ClickMouse(x,y):
    xrand=random.randint(0,5)
    yrand=random.randint(0,5)
    movetime=random.randint(10 ,100)/400
    waittime=random.randint(15,30)/10
    mouse.moveTo( x + xrand , y + yrand , movetime)
    mouse.click()
    time.sleep(waittime)

def RunGame():
    ClickMouse(x[0],y[0])
    ClickMouse(x[1],y[1])


def WorkGame():
    ClickMouse(1100,230)    #出征
    ClickMouse(650,300)     #出征
    ClickMouse(650,300)     #活動地圖
    ClickMouse(750,310)     #補充通行牌
    ClickMouse(520,500)     #補充一個
    ClickMouse(520,500)     #確認補充
    ClickMouse(620,450)     #確認確認
    ClickMouse(650,500)     #極難地圖
    ClickMouse(880,650)     #選擇隊伍出征
    ClickMouse(880,650)     #確定出征
    ClickMouse(660,555)     #確定使用通行牌
    time.sleep(10)

class PlayGame:
    def __init__(self,loops,age):
        self.name=name
        self.age=age


class hihou:
    def __init__(self,loops):
        self.loops = 120
    
    def WorkGame(loops):
        ClickMouse(1100,230)    #出征
        ClickMouse(650,300)     #出征
        ClickMouse(650,300)     #活動地圖
        ClickMouse(750,310)     #補充通行牌
        ClickMouse(520,500)     #補充一個
        ClickMouse(520,500)     #確認補充
        ClickMouse(620,450)     #確認確認
        ClickMouse(650,500)     #極難地圖
        ClickMouse(880,600)     #選擇隊伍出征
        ClickMouse(880,600)     #確定出征
        ClickMouse(660,555)     #確定使用通行牌
        time.sleep(10)
    
class reitai:
    def __init__(self,loops,rest):
        self.loops = 15   
         
    def StartGame():
        ClickMouse(1100,230)    #出征
        ClickMouse(650,300)     #出征
        ClickMouse(650,300)     #活動地圖
        ClickMouse(750,310)     #補充通行牌
        ClickMouse(520,500)     #補充一個
        ClickMouse(520,500)     #確認補充
        ClickMouse(620,450)     #確認確認
        ClickMouse(650,500)     #極難地圖
        ClickMouse(880,650)     #選擇隊伍出征
        ClickMouse(880,650)     #確定出征
        ClickMouse(670,600)     #確定使用通行牌
        time.sleep(10)
    
    def RunGame(rest=60):
        resttime=random.randint(rest,rest+20)
        time.sleep(resttime)
        ClickMouse(x[1],y[1])


worktime=0
clicktimes=0
while worktime< totalworks:
    worktime += 1
    print("Now start round " + str(worktime) + ".")
    reitai.StartGame()
    while clicktimes<=15:
        reitai.RunGame()
        clicktimes+=1
        if clicktimes % 10 == 0:
            print(str(clicktimes))
        else:
            print(".")
    ClickMouse(820,430)        
    clicktimes = 0
    
    
print("Done.")



