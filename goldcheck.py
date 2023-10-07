import requests

api_url = "https://127.0.0.1:2999/liveclientdata/activeplayer"
api_url_item = "http://ddragon.leagueoflegends.com/cdn/13.19.1/data/en_US/item.json"
#api_url = api_url + '?api_key=' + api_key

def check_gold(api_url):
    resp = requests.get(api_url, verify = False)

    payload = resp.json()
    current_gold = payload['currentGold']

    return current_gold

#request item data using API based on ID string
def item_request_image(api_url_item, build_path_final, build_path_mythic, ):
    resp = requests.get(api_url_item)

    for i in list(range(0,10000)):
        try:
            #payload = resp.json()['data'][str(i)]
            #name = resp.json()['data'][str(i)]['name']
            #gold = resp.json()['data'][str(i)]['gold']['base']
            payload = resp.json()['data'][str(i)]
            if payload['name'] in :
                print("found")
        except:
            pass

item_request(api_url_item)
