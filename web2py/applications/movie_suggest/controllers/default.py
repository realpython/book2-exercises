import requests
import json

def index():
    return dict()

def grab_movies():
    session.m = []
    TOKEN = '15068b3a-7529-4c6c-a306-4b46658fb6c2'
    url = requests.get('http://api.myapifilms.com/imdb/inTheaters?token={0}&format=json&language=en-us'.format(TOKEN))
    print(url)
    binary = url.content
    print('binary', binary)
    output = json.loads(binary)
    movies = output['data']['inTheaters']
    for movie in movies:
        all_movies = movie['movies']
        for meta in all_movies:
            if(meta['title']):
                print(meta["title"])
                session.m.append(pulse(meta["title"]))
    session.m.sort()
    return TABLE(*[TR(v) for v in session.m]).xml()

def pulse(movie):
    text = movie.replace('_', ' ')
    url = 'http://text-processing.com/api/sentiment/'
    data = {'text': text}
    r = requests.post(url, data=data)
    binary = r.content
    output = json.loads(binary)
    label = output["label"]
    pos = output["probability"]["pos"]
    neg = output["probability"]["neg"]
    neutral = output["probability"]["neutral"]
    return text, label, pos, neg, neutral
