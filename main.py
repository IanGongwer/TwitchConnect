import json
from twitch import *

base_url = 'https://api.twitch.tv/helix/'

client_id = '0u0hkgwkig2j0pvm4s3dl7wpbdgypk'
client_secret = 'ody9piwepcovwewqtu17f7gz5m72tq'
access_token = 't75fol0rpy5xy2b2aciekleeufgosa'

client = TwitchHelix(client_id=client_id, oauth_token=access_token)

def get_top_games(numofgames):
    data = client.get_top_games()
    count = 0
    for dict in data:
        if count <= numofgames:
            print('Game:', dict['name'], '| Game Id:', dict['id'])
            count+=1

def get_clips(streamer, numofclips):
    clips = client.get_clips(broadcaster_id=get_id(streamer))
    count = 0
    for clip in clips:
        if count <= numofclips:
            print(clip['url'])
            count+=1

def get_id(streamer):
    userinfo = client.get_users(streamer)
    data = userinfo[0]
    id = data['id']
    return id

def get_game_id(game):
    gameinfo = client.get_games(names=game)
    data = gameinfo[0]
    game_id = data['id']
    return game_id

def get_videos(streamer, numofvideos):
    videos = client.get_videos(user_id=get_id(streamer))
    count = 0
    for video in videos:
        if count <= numofvideos:
            print(video['title'] + ':', video['url'])
            count += 1

def get_live_streams(game, numofstreams):
    livestreams = client.get_streams(game_ids=get_game_id(game))
    count = 0
    for stream in livestreams:
        if count <= numofstreams:
            print(stream['title'] + ':', stream['user_name'], 'is streaming to', stream['viewer_count'], 'people')
            count+=1