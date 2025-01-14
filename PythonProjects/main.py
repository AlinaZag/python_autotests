import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '228f3fd782c9326dd882623a7b0e3d4d'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "zagreeva@yandex.ru",
    "password": "Iloveqa1111"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "193920",
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "193920"
} 

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)