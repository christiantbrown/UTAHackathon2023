import requests

api_url = "https://127.0.0.1:2999/liveclientdata/activeplayer"
#api_url = "http://ddragon.leagueoflegends.com/cdn/13.19.1/data/en_US/item.json"
#api_url = api_url + '?api_key=' + api_key

def check_gold(api_url):
    resp = requests.get(api_url, verify = False)

    payload = resp.json()
    current_gold = payload['currentGold']

    return current_gold


