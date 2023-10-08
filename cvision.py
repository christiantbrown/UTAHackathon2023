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

def enemy_detection():
    print_screen("find_enemy.png")
    main_image = cv2.imread("find_enemy.png")
    template = cv2.imread('HPref.PNG')

    result = cv2.matchTemplate(main_image, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8  

    if max_val >= threshold:
        # Template match found
        match_location = max_loc
        match_location = (max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2)
        shifted_location = (match_location[0], match_location[1] + 80)
        return shifted_location
        #cv2.rectangle(main_image, match_location, (match_location[0] + template.shape[1], match_location[1] + template.shape[0]), (0, 255, 0), 2) 
        #cv2.imshow('Result', main_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    else:
        print("Template not found")

