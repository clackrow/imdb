import requests
import json
import time

def searchMovie():    
    print("---------------------------------------")
    search = input("Filme que deseja: ")
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/" + search
    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "1cdd86cb4amshbd682eb5d7ea0e4p1d58b5jsncdc3418e14c7"
    }
    response = requests.request("GET", url, headers=headers)
    js = json.loads(response.text)
    ide = js['titles'][0]['id']
    url2 = url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/" + ide
    movie = requests.request("GET", url, headers=headers)
    mjs = json.loads(movie.text)
    print("Título: " + mjs['title'])
    print("Lançamento: " + mjs['year'])
    print("Nota: " + mjs['rating'])
    print("Enredo: " + mjs['plot'])
    searchMovie()

searchMovie()
