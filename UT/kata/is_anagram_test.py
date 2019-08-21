import pytest

from kata.is_anagram import is_anagram

def test_initial():
    assert is_anagram('test', 'test')


@pytest.mark.parametrize('message1, message2',{
    ('test', 'not_test'),
    ('not_test', 'test'),
    ('true', 'false'), #bezsensowny test bo ('test', 'not_test'),sprawdza to samo
    ('test', 'tesssst'),
})
def test_not_anagram(message1, message2):
    assert not is_anagram(message1, message2)


@pytest.mark.parametrize('message1, message2',{
    ('test', 'tets'),
    ('cart horse', 'orchestra')
})
def test_real_anagram(message1, message2):
    assert is_anagram(message1, message2)