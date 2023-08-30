# LeagueofLegends-AutoZhonya
Simple Python script to activate Zhonya's Hourglass or Stopwatch based on defined health threshold.


# Introduction

This repository contains a Python script that utilizes the League of Legends Game Client API to automatically use in-game items (stopwatch and zhonya) when the player's health falls below a certain threshold. The script uses the requests library to make API calls and the keyboard library to simulate keypresses for activating the items. The script also uses the json library to parse the API's JSON response.

The user can specify their desired health threshold and the names of the items they wish to use in the script.

# Setup

* Clone this repository to your local machine.
* In the command line, navigate to the project's root directory and run the following command to install the required dependencies:

```
pip3 install requests
```

```
pip3 install keyboard
```

* Open the script in a code editor and update the health_threshold variable to your desired value.
* Wait to start a match.
* Run the script using your preferred method (e.g. command line, code editor's built-in terminal, etc.)

# Requirements

* Python 3.10 +

* League of Legends Game

* League of Legends Game Client API

* Requests library

* Keyboard library

* json library

* cert file (included)


# Note
Items must be in the following slots after purchase:
* Potions, slot number 1
* Stopwatch or Zhonya, slot number 2
* SummonerSpell heal, preparation F

# Important
After consuming items, apply ALT+TAB to exit the game screen and come back, so that when the time is up the script applies again.
This can be done after 15 seconds which is when you have new potion.

* Countdown potion 15 seconds
* Countdown zhonya 120 seconds
* Countdown heal 240 seconds
