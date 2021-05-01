import requests
from flask import request

searchurl = "https://api.rawg.io/api/games?key=8303ff9c44c54030a13e5ea703d768f8&search="


response = requests.request("GET", "https://api.rawg.io/api/games?key=8303ff9c44c54030a13e5ea703d768f8&dates=2019-09-01")

print(response.text)

def search():
    if request.method == 'POST':
        #search
        searchurl = "https://api.rawg.io/api/games?key=8303ff9c44c54030a13e5ea703d768f8&search="
        searchentry = request.form['search']
        searchlink = searchurl + searchentry

        searchresponse = requests.request("GET", searchlink)

        return searchresponse
