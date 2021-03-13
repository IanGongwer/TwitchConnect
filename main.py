import json
from twitch import *

base_url = 'https://api.twitch.tv/helix/'

client_id = '0u0hkgwkig2j0pvm4s3dl7wpbdgypk'
client_secret = 'ody9piwepcovwewqtu17f7gz5m72tq'
access_token = 't75fol0rpy5xy2b2aciekleeufgosa'

client = TwitchHelix(client_id=client_id, oauth_token=access_token)

def get_top_games():
    data = client.get_top_games()
    count = 0
    for dict in data:
        if count < 11:
            print(dict['name'])
            count+=1