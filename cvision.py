import cv2
import pyautogui
import numpy as np

def print_screen(filename):
    screen_width, screen_height = pyautogui.size()
    ss = pyautogui.screenshot()
    ss.save(filename)

def search_image(reference_img) -> int:
    ref_img = cv2.imread(reference_img, 0)
    print_screen("unknown")
    search_img = cv2.imread("unknown.png", 0)

    res = cv2.matchTemplate(search_img, ref_img, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    center_x = max_loc[0] + ref_img.shape[1] // 2
    center_y = max_loc[1] + ref_img.shape[0] // 2

    return center_x, center_y
