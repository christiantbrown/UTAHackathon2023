from pynput.keyboard import Key, Controller

from TwitchPlays_KeyCodes import V, HoldKey, ReleaseKey, HoldAndReleaseKey
import TwitchPlays_KeyCodes
import time
import pyautogui
from build_path import *
from goldcheck import *


scrWidth, scrHeight = pyautogui.size()  


playerKeys = {1:TwitchPlays_KeyCodes.F1, 2:TwitchPlays_KeyCodes.F2, 3:TwitchPlays_KeyCodes.F3, 4:TwitchPlays_KeyCodes.F4, 5:TwitchPlays_KeyCodes.F5}
numKeys=[TwitchPlays_KeyCodes.ONE,TwitchPlays_KeyCodes.TWO,TwitchPlays_KeyCodes.THREE,TwitchPlays_KeyCodes.FOUR,TwitchPlays_KeyCodes.FIVE,TwitchPlays_KeyCodes.SIX,TwitchPlays_KeyCodes.SEVEN]
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

handler = {
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
    "bye":itemroutine
    
    
}




