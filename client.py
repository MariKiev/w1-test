import requests
import json
import click

@click.group()
def client():
    pass

@click.command()
@click.argument('id')
def get_user(id):
    response = requests.get('https://w1-test.herokuapp.com/api/users/%s' % id)
    if response.ok:
        click.echo(response.json())
    else:
        click.echo('No user')

@click.command()
@click.option('--username', required=True)
@click.option('--email', required=True)
@click.option('--password', required=True)
@click.option('--phone_number', required=True)
@click.option('--pets')
def create_user(username, email, password, phone_number, pets):
    response = requests.post('https://w1-test.herokuapp.com/api/users', data={'username': username, 
        'email': email,
        'password': password,
        'phone_number': phone_number,
        'pets': pets
        })
    if response.ok:
        click.echo(response.json())
    else: 
        click.echo(response.text)

client.add_command(get_user)
client.add_command(create_user)

if __name__ == '__main__':
    client()
    
