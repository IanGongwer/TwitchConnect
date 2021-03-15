import json
from twitch import *

client_id = '0u0hkgwkig2j0pvm4s3dl7wpbdgypk'
access_token = 't75fol0rpy5xy2b2aciekleeufgosa'

client_secret = 'ody9piwepcovwewqtu17f7gz5m72tq'

client = TwitchHelix(client_id=client_id, oauth_token=access_token)

def get_top_games(numofgames):
    data = client.get_top_games()
    count = 0
    for dict in data:
        if count < numofgames:
            print('Game:', dict['name'].capitalize(), '| Game Id:', dict['id'])
            count+=1

def get_clips(streamer, numofclips):
    clips = client.get_clips(broadcaster_id=get_id(streamer))
    count = 0
    for clip in clips:
        if count < numofclips:
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
        if count < numofvideos:
            print(video['title'].capitalize() + ':', video['url'])
            count += 1

def get_live_streams(game, numofstreams):
    livestreams = client.get_streams(game_ids=get_game_id(game))
    count = 0
    for stream in livestreams:
        if count < numofstreams:
            print(stream['title'].capitalize() + ':', stream['user_name'].capitalize(), 'is streaming to', stream['viewer_count'], 'people')
            count+=1

def get_follow_relationship(streamer1, streamer2):
    info = client.get_user_follows(from_id=get_id(streamer1), to_id=get_id(streamer2))
    if len(info) != 0:
        print(streamer1.capitalize(), 'has a follow affiliation with', streamer2.capitalize())
    else:
        print(streamer1.capitalize(), 'has no follow affiliation with', streamer2.capitalize())

get_top_games(5)