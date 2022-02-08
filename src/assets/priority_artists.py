from lists import bigArtists, cityList
import json

f = open('data.json')
data = json.load(f)

def getArtists(city):
    for i in data[city]:
        artist_name = i['name']
        artist_name_lower = i['name'].lower()

        for big_artist in bigArtists:
            if big_artist in artist_name_lower:
                print(artist_name)
    

if __name__ == '__main__':
    for city in cityList:
        getArtists(city)