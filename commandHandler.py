from pynput.keyboard import Key, Controller

from TwitchPlays_KeyCodes import V, HoldKey, ReleaseKey, HoldAndReleaseKey
import TwitchPlays_KeyCodes
import time
import pyautogui
from build_path import *
from goldcheck import *
from cvision import *


scrWidth, scrHeight = pyautogui.size()  


playerKeys = {**dict.fromkeys(['won','one','1',1],TwitchPlays_KeyCodes.F1), **dict.fromkeys(['too','to','2',2],TwitchPlays_KeyCodes.F2), **dict.fromkeys(['three','3','tree',3],TwitchPlays_KeyCodes.F3), **dict.fromkeys(['four','for',4,'4'],TwitchPlays_KeyCodes.F4), **dict.fromkeys([5,'five','5'],TwitchPlays_KeyCodes.F5)}
numKeys={**dict.fromkeys(['won','one','1',1],TwitchPlays_KeyCodes.ONE),**dict.fromkeys(['too','to','2',2],TwitchPlays_KeyCodes.TWO),**dict.fromkeys(['three','3','tree',3],TwitchPlays_KeyCodes.THREE),**dict.fromkeys(['four','for',4,'4'],TwitchPlays_KeyCodes.FOUR),**dict.fromkeys([5,'five','5'],TwitchPlays_KeyCodes.FIVE),**dict.fromkeys(['six','6',6],TwitchPlays_KeyCodes.SIX),**dict.fromkeys(['seven','7',7],TwitchPlays_KeyCodes.SEVEN)}
keyboard=Controller

def centerMouse():
    pyautogui.moveTo(scrWidth/2,scrHeight/2)

def heal():
    HoldAndReleaseKey(TwitchPlays_KeyCodes.E, .1)
    
def stick(num=4):
    print("stick called")
    print(num)


    
    if num not in [1,2,3,4,5]: num = 4
    HoldKey(playerKeys[num])    
    centerMouse()
    HoldAndReleaseKey(TwitchPlays_KeyCodes.W, .1)
    ReleaseKey(playerKeys[num])
    
def jump():
    HoldAndReleaseKey(TwitchPlays_KeyCodes.W, .1)
    
def item(num):
    if not num or num not in [1,2,3,4,5,6,7]: return
    centerMouse()
    HoldAndReleaseKey(numKeys[num],.1)
    
    
def itemroutine(*args): buy_items(build_path_final, check_gold(api_url))

def missile():
    for i in range(6):
        pyautogui.moveTo(enemy_detection())
        time.sleep(.5)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.Q, .1)

def wave():
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




