from pynput.keyboard import Key, Controller

from TwitchPlays_KeyCodes import HoldKey, ReleaseKey, HoldAndReleaseKey
import TwitchPlays_KeyCodes
import time
import pyautogui
from build_path import *
from goldcheck import *
from cvision import *


scrWidth, scrHeight = pyautogui.size()  


playerKeys = {1:TwitchPlays_KeyCodes.F1, 2:TwitchPlays_KeyCodes.F2, 3:TwitchPlays_KeyCodes.F3, 4:TwitchPlays_KeyCodes.F4, 5:TwitchPlays_KeyCodes.F5}

keyboard=Controller

def heal():
    HoldAndReleaseKey(TwitchPlays_KeyCodes.E, .1)
    
def stick(num=4):
    print("stick called")
    print(num)


    
    if num not in [1,2,3,4,5]: num = 4
    HoldKey(playerKeys[num])    
    pyautogui.moveTo(scrWidth/2,scrHeight/2)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.W, .1)
    ReleaseKey(playerKeys[num])
    
def jump():
    HoldAndReleaseKey(TwitchPlays_KeyCodes.W, .1)

def missile():
    pyautogui.moveTo(enemy_detection())
    HoldAndReleaseKey(TwitchPlays_KeyCodes.Q, .1)

def wave():
    pyautogui.moveTo(enemy_detection())
    HoldAndReleaseKey(TwitchPlays_KeyCodes.R, .1)

def pop_summs():
    pyautogui.moveTo(enemy_detection())
    HoldAndReleaseKey(TwitchPlays_KeyCodes.D, .1)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.F, .1)


handler = {
    "pop":pop_summs,
    "wave":wave,
    "missile":missile,
    "e":heal,
    "heal":heal,
    "shield":heal,
    "heel":heal,
    "hill":heal,
    "stick":stick,
    "shop":buy_items(build_path_final, check_gold(api_url))
}




