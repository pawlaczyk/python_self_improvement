from unittest.mock import patch, Mock, MagicMock

import pytest
import requests

from twitter import Twitter

#BLOKOWANIE REQUEST
class ResponseGetMock(object):
    """Mockowanie resp = request.get(url); resturn resp.json()['avatar_url']"""
    def json(self):
        return {'avatar_url': 'test'}

@pytest.fixture(params=[None, 'python']) #kombinajce parametrow dla testów, zeby nie pisac ifów w `fixture_twitter`
def username(request): #nowy sparametryzowany fixture
    """Zwiększona ilosć kombinacji testowych - tworzy 33 testy UT"""
    return request.param


@pytest.fixture(params=['list', 'backend'], name='twitter') #zmiana nazw parametrów testu na opisowy by wiedziec jaki typ testu chcemy wykonać
def fixture_twitter(backend, username, request, monkeypatch): #brak argumentu monkeypatch, niepotrzeba
    if request.param == 'list':
        twitter = Twitter(username=username)
    if request.param == 'backend':
        twitter = Twitter(backend=backend, username=username)

    return twitter


def test_twitter_initialization(twitter):
    assert twitter


# ------------------- LEPSZA WERSJA - dekorator i patchowanie biblioteki requests
@patch.object(requests, 'get', return_value=ResponseGetMock())# mockowanie biblioteki
def test_tweet_single_message(avatar_mock, twitter): #mock będzie przekazany jako pierwszy argument funkcji testującej
    """Przed deklaracją funkcji nie mamy dostępu do danych wejściowych; dlatego dekorator musi użyć klasy `Twitter`
    funckja z poprzedniej wersji testów `no_request` nie jest już potrzebna"""
    twitter.tweet("Test message")
    assert twitter.tweet_messages == ["Test message"]


def test_tweet_long_message(twitter):
    # assert twitter # nie trzeba testować przypadku który jest już testowany drugi raz
    with pytest.raises(Exception):
        twitter.tweets('test'*41)
    assert twitter.tweet_messages == []


@pytest.mark.parametrize("message, expected", (
    ("Test #first message", ["first"]),
    ("#first Test message", ['first']),
    ("#FIRST Test message", ['first']),
    ("Test message #first", ['first']),
    ("Test message #first #second", ['first', 'second']),
))
def test_tweet_with_hashtag(twitter,
                            message, expected):
    assert twitter.find_hashtags(message) \
           == expected

def test_initialize_two_twitter_classes(backend):
    """Test ten przyjmuje backend więc jest wywołany tylko raz"""
    #GIVEN - sytuacja wejśiowa do testów
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    # WHEN - dzieje się jakaś akcja
    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')

    #THEN - czyli assercja
    assert twitter2.tweet_messages == ['Test 1', 'Test 2']


# ------------------- LEPSZA WERSJA - patchowanie biblioteki requests
@patch.object(requests, 'get', return_value=ResponseGetMock())# mockowanie biblioteki
def test_tweet_with_username(avatar_mock, twitter): # przekazujemy mocka bo inaczej nie zostanie użyty
    if not twitter.username:
        pytest.skip()  # opuszczanie testu, gdy brak username

    twitter.tweet('Test message')
    assert twitter.tweets == [{'message': 'Test message', 'avatar': 'test', 'hashtags': []}]
    # sprawdzanie wywołań, np zmieniajać funcknojanlnosc klasy titter na
    # self.tweets.append({'message' : message, 'avatar':'test'}) wyżej test przejdzie, ale mock zwróci błąd, bo nie
    # została na nim wywołana metoda `get_user_avatar` - Bład: AssertionError: Expected 'get_user_avatar' to have been called
    avatar_mock.assert_called() #sprawdza czy metoda mockowana została w ogóle wywołana assert_called_once() asser_called_witch(arg1, arg2) linia bez asserta


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_hashtags(avatar_mock, twitter):
    twitter.find_hashtags = Mock()
    twitter.find_hashtags.return_value = ['first']
    twitter.tweet('Test #second')
    assert twitter.tweets[0]['hashtags'] == ['first']
    twitter.find_hashtags.assert_called()


def test_twitter_version(twitter):
    #różnica między Mock i MagicMock
    # twitter.version = Mock()
    # twitter.version.__eq__.return_value = '2.0' #Mock() nie wspiera NADPISYWANIA MAGICZNYCH METOD PYTHONA!

    twitter.version = MagicMock()
    twitter.version.__eq__.return_value == '2.0'

    assert twitter.version == '2.0'

@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_twitter_get_all_hashtags(avatar_mock, twitter):
    twitter.tweet('Test #first')
    twitter.tweet('Test #first #second')
    twitter.tweet('Test #third')

    assert twitter.get_all_hashtags() == {'first', 'second', 'third'}

@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_twitter_get_all_hashtags_not_found(avatar_mock, twitter):
    twitter.tweet('Test first')
    assert twitter.get_all_hashtags() == 'No hashtags found'