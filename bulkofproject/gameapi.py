import requests
from flask import request
import random
from random import *


def randomGame(titleslist):
    count = 0
    if request.form['search'] == "":
        displayMessage = "Please search a game. Here are some popular games:"
        return displayMessage
    else:
        for item in titleslist:
            count = count + 1
        randomNumber = randint(0, count)
        randomSelect = titleslist[randomNumber]
        displayMessage = "Your random game is: " + randomSelect
        return displayMessage


