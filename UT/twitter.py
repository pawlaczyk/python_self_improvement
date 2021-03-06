import json
import os
import re

#api github
from urllib.parse import urljoin

import requests

USERS_API = 'https://api.github.com/users/'

class Twitter(object):
    version = '1.0'

    def __init__(self, backend=None, username=None):
        """Dodatkowy parametr z """
        self.backend = backend
        self._tweets = []
        self.username = username

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            backend_text = self.backend.read()
            if backend_text:
                self._tweets = json.loads(backend_text)
        return self._tweets

    @property
    def tweet_messages(self):
        """Zwraca wyłącznie wiadomości tweetów"""
        return [tweet['message'] for tweet in self.tweets]

    def get_user_avatar(self):
        """Wykonanie requestu do api gihuba oraz przeczytanie odpowiedzi i wyciągnięcie z niej url z avatarem użytkownika"""
        if not self.username:
            return None #jak brak nazwy użytkownika to nie zwracamy avatara
        url = urljoin(USERS_API, self.username)
        # import web_pdb; web_pdb.set_trace()
        resp = requests.get(url)
        return resp.json()['avatar_url'] #parsowanie odpowiedzi z jsona z serwera

    def tweet(self, message):
        if len(message) > 160:
            raise Exception("Message to long")
        self.tweets.append({
            "message": message,
            'avatar': self.get_user_avatar(),
            'hashtags': self.find_hashtags(message)
        })
        # self.tweets.append({"message": message, 'avatar': 'test'})
        if self.backend:
            self.backend.write(json.dumps(self.tweets))

    def find_hashtags(self, message):
        """Zwraca hastagi małymi literami"""
        return [m.lower() for m in re.findall("#(\w+)", message)]

    def get_all_hashtags(self):
        hashtags = []
        for message in self.tweets:
            hashtags.extend(message['hashtags'])
        if hashtags:
            return set(hashtags)
        return "No hashtags found"

twitter = Twitter()
print(twitter.version, twitter.tweets)
twitter.tweet("Wiadomosc")
print(twitter.version, twitter.tweets)
