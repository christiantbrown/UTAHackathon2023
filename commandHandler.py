from pynput.keyboard import Key, Controller

from TwitchPlays_KeyCodes import V, HoldKey, ReleaseKey, HoldAndReleaseKey
import TwitchPlays_KeyCodes
import time
import pyautogui
from build_path import *
from goldcheck import *
from cvision import *


scrWidth, scrHeight = pyautogui.size()  

f1 = TwitchPlays_KeyCodes.F1;f2=TwitchPlays_KeyCodes.F2;f3=TwitchPlays_KeyCodes.F3;f4=TwitchPlays_KeyCodes.F4;f5=TwitchPlays_KeyCodes.F5
one=TwitchPlays_KeyCodes.ONE;two=TwitchPlays_KeyCodes.TWO;three=TwitchPlays_KeyCodes.THREE;four=TwitchPlays_KeyCodes.FOUR;five=TwitchPlays_KeyCodes.FIVE;six=TwitchPlays_KeyCodes.SIX;seven=TwitchPlays_KeyCodes.SEVEN
playerKeys={'one':f1,'1':f1,1:f1,'two':f2,'too':f2,'to':f2,'2':f2,2:f2,'three':f3,'tree':f3,'3':f3,3:f3,'four':f4,'for':f4,'4':f4,4:f4,'five':f5,'5':f5,5:f5}
numKeys={'one':one,'won':one,'1':one,1:one,'two':two,'too':two,'to':two,'2':two,2:two,'three':three,'tree':three,'3':three,3:three,'four':four,'for':four,'4':four,4:four,'five':five,'5':five,5:five,'six':six,'6':six,6:six,'seven':seven,'7':seven,7:seven}
keyboard=Controller

def centerMouse():
    pyautogui.moveTo(scrWidth/2,scrHeight/2)

def heal(*args):
    HoldAndReleaseKey(TwitchPlays_KeyCodes.E, .1)
    
def stick(num=4):
    print("stick called")
    print(num)


    num = playerKeys[num]
    if num not in [f1,f2,f3,f4,f5]: num=f4

    HoldKey(num)    
    centerMouse()
    HoldAndReleaseKey(TwitchPlays_KeyCodes.W, .1)
    ReleaseKey(num)
    
def jump(*args):
    HoldAndReleaseKey(TwitchPlays_KeyCodes.W, .1)
    
def item(num):
    if not num or num not in [1,2,3,4,5,6,7]: return
    centerMouse()
    HoldKey(numKeys[num])
    pyautogui.click()
    time.sleep(.05)
    pyautogui.click()
    ReleaseKey(numKeys[num])
    
    
def itemroutine(*args): buy_items(build_path_final, check_gold(api_url))

def missile(*args):
    for i in range(6):
        pyautogui.moveTo(enemy_detection())
        time.sleep(.5)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.Q, .1)

def wave(*args):
    pyautogui.moveTo(enemy_detection())
    HoldAndReleaseKey(TwitchPlays_KeyCodes.R, .1)


handler = {
    "wave":wave,
    "missile":missile,
    "e":heal,
    "heal":heal,
    "shield":heal,
    "heel":heal,
    "hill":heal,
    "stick":stick,
    "item" : item,
    "use": item,
    
    "shop":itemroutine,
    "stop":itemroutine,
    "shut":itemroutine,
    "buy":itemroutine,
    "bye":itemroutine,
    
    

}




