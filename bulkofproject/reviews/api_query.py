#imports
import requests
import json

def gamequery():
    #empty list
    games = []
    page = 27983
    #repeat for every page
    for i in range(1,page):
        #call api as a list
        i = str(i)
        apiurl = requests.get("https://api.rawg.io/api/games?key=91edf65dde2d49c7a6519987ed7c1769&page=27982"+i)
        api = apiurl.json()
        games.append(type(api))
        #apilist = api['results']
    #append list
        #for game in apilist:
            #name = game['name']
            #games.append(name)

    return games

print(gamequery())