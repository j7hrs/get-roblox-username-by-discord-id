import requests
import os
os.system('title Get Roblox Username By Discord ID')

while True:
    amogus = input('Please enter target Discord ID: ')
    if amogus != '':
        res1 = requests.get('https://api.blox.link/v1/user/' + amogus)
        if res1.json()['status'] != 'error':
            print('Bloxlink (id only lol):', res1.json()['primaryAccount'])
        else:
            print('Bloxlink (id only lol): Error! (' + res1.json()['error'] + ')')
        res2 = requests.get('https://verify.eryn.io/api/user/' + amogus)
        if res2.json()['status'] != 'error':
            print('Rover: @' + res2.json()['robloxUsername'])
        else:
            print('Rover: Error! (' + res2.json()['error'] + ')')
    else:
        print('bruh moment')
