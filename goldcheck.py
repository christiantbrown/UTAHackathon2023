import requests
from build_path import *
import cv2
from skimage import io
import os

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
    folder_name = "item_images"
    os.makedirs(folder_name, exist_ok=True)

    if not os.listdir("item_images"):
        for i in list(range(1000,5000)):
            try:
                payload = resp.json()['data'][str(i)]

                if payload['name'] in str(build_path_final):
                    img_url = "https://ddragon.leagueoflegends.com/cdn/13.19.1/img/item/" + str(i) + ".png"
                    print(img_url)
                    image = requests.get(img_url).content
                    with open(os.path.join(folder_name, str(i) + ".png"), 'wb') as f:
                        f.write(image)
                    print(f"Image {i} downloaded successfully.")

                    f.write(image)
                    f.close()
            except:
                pass

item_request_image(api_url_item, build_path_final)
#print(build_path_final)