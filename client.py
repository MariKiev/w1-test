import requests
import json

def get_user(id):
    response = requests.get('https://w1-test.herokuapp.com/api/users/%s' % id)
    return json.loads(response.text)

def create_user(username, email, phone_number, pets):
    response = requests.post('https://w1-test.herokuapp.com/api/users', data={'username': username, 
        'email': email,
        'phone_number': phone_number,
        'pets': pets
        })
    return json.loads(response.text)