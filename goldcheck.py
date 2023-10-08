import requests
#from build_path.py import build_path_final
import cv2
from skimage import io

api_url = "https://127.0.0.1:2999/liveclientdata/activeplayer"
api_url_item = "http://ddragon.leagueoflegends.com/cdn/13.19.1/data/en_US/item.json"
#api_url = api_url + '?api_key=' + api_key

#checks gold on current player
def check_gold(api_url):
    resp = requests.get(api_url, verify = False)

    payload = resp.json()
    current_gold = payload['currentGold']

    return current_gold

#request item data using API based on ID string
def item_request_image(api_url_item, build_path_final):
    resp = requests.get(api_url_item)

    for i in list(range(1000,10000)):
        try:
            payload = resp.json()['data'][str(i)]

            if payload['name'] in build_path_mythic[:][0] or build_path_final[:][0]:
                print('found')
                img_url = "https://ddragon.leagueoflegends.com/cdn/13.19.1/img/item/" + str(i) + ".png"
                print(img_url)
                image = requests.get(img_url).content
                f = open(str(i) + ".png", 'wb')

                f.write(image)
                f.close()
        except:
            pass

build_path_mythic = [('Bandleglass Mirror', 950),
                    ('Kindlegem', 800)]

build_path_staff_ardent = [("Forbidden Idol", 800),
                            ("Aether Wisp", 850)]

build_path_redemption_mikael = [("Forbidden Idol", 800), 
                                ("Chalice of Blessing", 950)]

build_path_final = [("Spellthief's Edge", 450, None),
                    ("Shurelya's Battlesong", 2300, build_path_mythic),
                    ("Staff of Flowing Water", 2100, build_path_staff_ardent),
                    ("Ardent Censer", 2100, build_path_staff_ardent),
                    ("Redemption", 2300, build_path_redemption_mikael),
                    ("Mikael's Blessing", 2300, build_path_redemption_mikael)
                    ]
item_request_image(api_url_item, build_path_mythic)
#print(build_path_final)