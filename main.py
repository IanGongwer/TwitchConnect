from twitch import *

base_url = 'https://api.twitch.tv/helix/'

client_id = '0u0hkgwkig2j0pvm4s3dl7wpbdgypk'
client_secret = 'ody9piwepcovwewqtu17f7gz5m72tq'
access_token = 't75fol0rpy5xy2b2aciekleeufgosa'

client = TwitchHelix(client_id=client_id, oauth_token=access_token)
print(client.get_streams())