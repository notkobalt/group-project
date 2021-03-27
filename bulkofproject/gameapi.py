import requests

url = "https://rawg-video-games-database.p.rapidapi.com/games"

headers = {
    'x-rapidapi-key': "f4e47a0331msh068fd5299f4fe60p13031ejsn3acdd247ddd3",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

#print(response.text)