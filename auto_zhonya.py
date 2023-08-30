import requests
import json
import time
import keyboard


def find_summoner_name(data):
    return data["activePlayer"]["summonerName"]

def find_max_health(data):
        return data["activePlayer"]["championStats"]["maxHealth"]


def check_health(data, health_threshold):
    if data["activePlayer"]["championStats"]["currentHealth"] <= health_threshold:
        return True
    else:
        return False


def is_alive(data, player):
    for p in data["allPlayers"]:
        if p["summonerName"] == player and p["isDead"] == False:
            return True
    return False


def use_item(data, health_threshold):
    if check_health(data, health_threshold):
            print('Zhonya')
            keyboard.press(str(2))
            time.sleep(3)
            print('Spell Two F')
            keyboard.press('F')
            time.sleep(1)
            print('Potion')
            keyboard.press(str(1))
            

cert_path = "LoL Game Engineering Certificate Authority.crt"

response = requests.get(
    "https://127.0.0.1:2999/liveclientdata/allgamedata", verify=cert_path
)
data = json.loads(response.text)

player = find_summoner_name(data)


while player:
    response = requests.get(
        "https://127.0.0.1:2999/liveclientdata/allgamedata", verify=cert_path
    )
    data = json.loads(response.text)

    if is_alive(data, player):
        max_health = int(find_max_health(data))
        print('Max Health  ', max_health)
        percent_max_health = 35
        health_threshold = int(max_health * percent_max_health / 100)
        print('Zhonya apply ', health_threshold)
        use_item(data, health_threshold)

    time.sleep(0.3)
