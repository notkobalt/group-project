import requests
from flask import request
import random
from random import *


def randomGame(titleslist):
    count = 0
    if request.form['search'] == "":
        displayMessage = "please specify a specific game! here are some examples:"
        return displayMessage
    else:
        for item in titleslist:
            count = count + 1
        randomNumber = randint(0, count)
        randomSelect = titleslist[randomNumber]
        displayMessage = "your random game is: " + randomSelect
        return displayMessage


