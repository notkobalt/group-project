import requests
from flask import request
import json

searchurl = "https://api.rawg.io/api/games?key=91edf65dde2d49c7a6519987ed7c1769&search=silent-hill"
titleslist = []

searchresponse = requests.request("GET", searchurl)

searchdump = searchresponse.json()
searchresults = searchdump['results']
displaylinks = ''

for item in searchresults:
    titleslist.append(item['name'])

for index in titleslist:
    displaylinks = displaylinks +  "<a href=#>" + index + "</a></br> "

print(displaylinks)




def search():
    if request.method == 'POST':
        #search
        searchurl = "https://api.rawg.io/api/games?key=8303ff9c44c54030a13e5ea703d768f8&search="
        searchentry = request.form['search']
        searchlink = searchurl + searchentry

        searchresponse = requests.request("GET", searchlink)

        return searchresponse.text
