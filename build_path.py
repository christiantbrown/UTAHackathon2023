import TwitchPlays_KeyCodes
from TwitchPlays_KeyCodes import HoldAndReleaseKey, HoldKey, ReleaseKey
import pyautogui
import time

build_path_mythic = [("Bandleglass Mirror", 950, "4642"),
                    ("Kindlegem", 800, "3067")]

build_path_staff = [("Forbidden Idol", 800, "3114"),
                    ("Aether Wisp", 850, "3113")]

build_path_redemption = [("Forbidden Idol", 800, "3114"), 
                        ("Chalice of Blessing", 950, "3012")]
                                
build_path_ardent = [("Forbidden Idol", 800, "3114"),
                    ("Aether Wisp", 850, "3113")]

build_path_mikael = [("Forbidden Idol", 800, "3114"), 
                    ("Chalice of Blessing", 950, "3012")]

build_path_final = [("Spellthief's Edge", 450, None, "3850"),
                    ("Shurelya's Battlesong", 2300, build_path_mythic, "2065"),
                    ("Staff of Flowing Water", 2100, build_path_staff, "6616"),
                    ("Ardent Censer", 2100, build_path_ardent, "3504"),
                    ("Redemption", 2300, build_path_redemption, "3107"),
                    ("Mikael's Blessing", 2300, build_path_mikael, "3222")
                    ]

def purchase_item(item):
    HoldAndReleaseKey(TwitchPlays_KeyCodes.P, 0.1)
    time.sleep(0.3)
    HoldKey(TwitchPlays_KeyCodes.LEFT_CONTROL)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.L, .1)
    time.sleep(0.3)
    ReleaseKey(TwitchPlays_KeyCodes.LEFT_CONTROL)
    pyautogui.write(item[0], interval=0.1)
    time.sleep(0.3)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.ENTER, 0.1)
    time.sleep(0.3)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.ESC, 0.1)


#recursively goes through list and invokes purchase_item if current gold is greather than item cost
def buy_items(items, current_gold):
    print(items)
    if not items:
        #if item list is empty, end the recursion
        return
    #iterates through item list
    for item in items.copy():
        #if current gold is greather than item cost, then buy it
        if item[1] < current_gold:
            purchase_item(item)
            #items.remove(item)
        #if not, then if item has a sublist for components, then it goes through that list instead
        elif isinstance(item, list):
            buy_items(item, current_gold)
        