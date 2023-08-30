import requests
import json
import time
import keyboard


def find_summoner_name(data):
    return data["activePlayer"]["summonerName"]


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


def use_item(data, player, health_threshold):
    if check_health(data, health_threshold):
            print('\x1b[6;30;43m' + 'Zhonya activated      ' + '\x1b[0m')
            keyboard.press(str(2))
            time.sleep(3)
            print('\x1b[5;30;42m' + 'Spell Two F activated ' + '\x1b[0m')
            keyboard.press('F')
            time.sleep(1)
            print('\x1b[2;30;44m' + 'Potion activated      ' + '\x1b[0m')
            keyboard.press(str(1))
            time.sleep(15)

cert_path = "LoL Game Engineering Certificate Authority.crt"

response = requests.get(
    "https://127.0.0.1:2999/liveclientdata/allgamedata", verify=cert_path
)
data = json.loads(response.text)

player = find_summoner_name(data)

health_threshold = 400

while player:
    response = requests.get(
        "https://127.0.0.1:2999/liveclientdata/allgamedata", verify=cert_path
    )
    data = json.loads(response.text)

    if is_alive(data, player):
        use_item(data, player, health_threshold)

    time.sleep(0.3)
