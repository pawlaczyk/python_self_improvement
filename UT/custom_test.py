import os

import pytest


# @pytest.mark.skip
# def test_sum():
#     assert 2+2 == 4

@pytest.mark.skipif(os.environ.get('NO_SUMMING') == '1', reason='NO_SUMMING set to 1')
def test_sum2():
    assert 2+2 == 4

@pytest.mark.xfail #chcemy żeby się nie udał
def test_get_element_from_list():
    """Np. gdy tworzymy dużą bibliotekę i ejsteśmy świadomi błedów; ale jednocześnie nie mają wpływu na zasadnicza cześć funckjonalności bibioteki
    informacja dla nas, że wiemy, że testy kończa się porażką; ale jednocześnie chcemy zapamiętać że trzeba na sytuację zwrócić uwagę"""
    custom_list = ["test"]
    assert custom_list[0] == "test"
