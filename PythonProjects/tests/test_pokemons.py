import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '228f3fd782c9326dd882623a7b0e3d4d'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '26300'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_id', TRAINER_ID), ('id', '193920')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value