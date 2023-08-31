# LeagueofLegends-AutoZhonya
Simple Python script to activate Zhonya's Hourglass or Stopwatch based on defined health threshold.


# Introduction

This repository contains a Python script that utilizes the League of Legends Game Client API to automatically use in-game items (stopwatch and zhonya) when the player's health falls below a certain threshold. The script uses the requests library to make API calls and the keyboard library to simulate keypresses for activating the items. The script also uses the json library to parse the API's JSON response.

The user can specify their desired health threshold and the names of the items they wish to use in the script.


# Requirements

* Python 3.10 +

* League of Legends Game

* League of Legends Game Client API

* Requests library

* Keyboard library

* json library

* cert file (included)

  
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


# Note
Item must be in the following slots after purchase:

* Stopwatch or Zhonya, slot number 2


# Important

if you don't want to use zhonya, hold the space key until you're in the base again, or life returns above 50%, which is how much is parameterized to apply zhonya.

After consuming zhonya, apply ALT+TAB during the item's cooldown time
(120 seconds) to exit the game screen and come back, the script is applied again.

* Countdown zhonya 120 seconds
