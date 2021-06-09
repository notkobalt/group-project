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

titlesdictionary = {}
searchurl = "https://api.rawg.io/api/games?key=91edf65dde2d49c7a6519987ed7c1769&search=omori"

#get entry from POST form

#send request to RAWG API game database
searchresponse = requests.request("GET", searchurl)
searchdump = searchresponse.json()
searchresults = searchdump['results']

#append all titles to a dictionary
for item in searchresults:
    titlesdictionary[item['name']] = item['background_image']

#format for HTML
displaylinks = ""
for x, y in titlesdictionary.items():
    if y == None:
        displaylinks = displaylinks + "<a href=#><div class='container'> <img class='icon' src='bulkofproject/static/greysquare.jpg'><div class='title'>" + x + "</div></div></a>"
    else:
        displaylinks = displaylinks + "<a href=#><div class='container'> <img class='icon' src='" + y + "'><div class='title'>" + x + "</div></div></a>"
print(displaylinks)


