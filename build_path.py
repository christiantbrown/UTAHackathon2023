import time
from cvision import search_image
from TwitchPlays_KeyCodes import HoldAndReleaseKey, HoldKey, ReleaseKey
import TwitchPlays_KeyCodes
import os.path
import pyautogui
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

build_path_final = [("Spellthief's Edge", 400, None, "3850"),
                    ("Oracle Lens", 0, None, "3364"),
                    ("Shurelya's Battlesong", 2300, build_path_mythic, "2065"),
                    ("Staff of Flowing Water", 2100, build_path_staff, "6616"),
                    ("Ardent Censer", 2100, build_path_ardent, "3504"),
                    ("Redemption", 2300, build_path_redemption, "3107"),
                    ("Mikael's Blessing", 2300, build_path_mikael, "3222")
                    ]

def purchase_item(item):
    impath=(os.path.join("item_images", (item[0] + ".png")))
    print(impath)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.P,.2)
    HoldKey(TwitchPlays_KeyCodes.LEFT_CONTROL)
    HoldAndReleaseKey(TwitchPlays_KeyCodes.L,.1)
    ReleaseKey(TwitchPlays_KeyCodes.LEFT_CONTROL)
    time.sleep(.2)
    targetX, targetY = search_image(os.path.join("item_images", (item[0] + ".png")))
    print(targetX, targetY)
    pyautogui.moveTo(targetX, targetY)
    pyautogui.click()
    time.sleep(.05)
    pyautogui.click()
    return item

#recursively goes through list and invokes purchase_item if current gold is greather than item cost
def buy_items(items, current_gold):
    if not items:
        #if item list is empty, end the recursion
        return
    #iterates through item list
    for item in items.copy():
        #if current gold is greather than item cost, then buy it
        if item[1] < current_gold:
            purchase_item(item)
            items.remove(item)
        #if not, then if item has a sublist for components, then it goes through that list instead
        elif isinstance(item, list):
            buy_items(item, current_gold)
        