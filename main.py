import requests
import os
os.system('title Get Roblox Username By Discord ID')

while True:
    amogus = input('Please enter target Discord ID: ')
    if amogus != '':
        bloxlinkkey = input('Enter Bloxlink Global API key (leave blank to not use Bloxlink\'s global API): ')
        if bloxlinkkey != '':
            res1 = requests.get('https://api.blox.link/v4/public/discord-to-roblox/' + amogus, headers={"Authorization":bloxlinkkey})
            if res1.status_code == 200:
                print(f'Bloxlink (id only lol): {res1.json()['primaryAccount']}')
            else:
                print(f'Bloxlink (id only lol): Error! ({res1.json()['error']})')
        else:
            print("Bloxlink: not used")
        roverkey = input('Enter RoVer API key (leave blank to not use Rover\'s API): ')
        if roverkey != '':
            gid = input('Enter Discord server ID (required, since there\'s no endpoint for global api): ')
            if gid != '':
                res2 = requests.get(f'https://registry.rover.link/api/guilds/{gid}/discord-to-roblox/{amogus}', headers={"Authorization": f"Bearer {roverkey}"})
                if res2.status_code == 200:
                    print(f'Rover: {res2.json()['robloxId']}')
                else:
                    print(f'Rover: Error! ({res2.json()['error']})')
            else:
                print("Rover: no server ID applied")
        else:
            print("Rover: not used")
    else:
        print('bruh moment')
