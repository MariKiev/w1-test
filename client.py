import requests
import json

def get_user(id):
    response = requests.get('http://localhost:5000/api/users/%s' % id)
    return json.loads(response.text)

def create_user(username, email, phone_number, pets):
    response = requests.post('http://localhost:5000/api/users', data={'username': username, 
        'email': email,
        'phone_number': phone_number,
        'pets': pets
        })
    return json.loads(response.text)