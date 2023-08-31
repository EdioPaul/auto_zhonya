import requests
import json
import time
import keyboard
import pyautogui


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
    if not keyboard.is_pressed('space'): 
        if check_health(data, health_threshold):
            print('Zhonya')
            keyboard.press(str(2))
            time.sleep(120)            

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
        percent_max_health = 50
        health_threshold = int(max_health * percent_max_health / 100)
        use_item(data, health_threshold)

    time.sleep(0.3)
