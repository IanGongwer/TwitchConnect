import json
from twitch import *

client_id = ""
client_secret = ""

client = TwitchHelix(client_id=client_id, client_secret=client_secret)
client.get_oauth()

# Get # of top games on twitch
def get_top_games(numofgames):
    data = client.get_top_games()
    count = 0
    top_games = []
    for dict in data:
        if count < numofgames:
            top_games.append(str(dict['name'].title()))
            count+=1
        if count == numofgames:
            return top_games

# Get # of top clips for a streamer (Ordered by most popular)
def get_clips(streamer, numofclips):
    clips = client.get_clips(broadcaster_id=get_id(streamer))
    count = 0
    clips_list = []
    for clip in clips:
        if count < numofclips:
            clips_list.append(str(clip['url']))
            count+=1
        if count == numofclips:
            return clips_list

# Get id of streamer
def get_id(streamer):
    try:
        userinfo = client.get_users(streamer)
        data = userinfo[0]
        id = data['id']
        return id
    except:
        return "User does not exist"

# Get id # of a game on twitch
def get_game_id(game):
    gameinfo = client.get_games(names=game)
    data = gameinfo[0]
    game_id = data['id']
    return game_id

# Get # of videos for a streamer (Ordered by most recent)
def get_videos(streamer, numofvideos):
    videos = client.get_videos(user_id=get_id(streamer))
    count = 0
    videos_list = []
    for video in videos:
        if count < numofvideos:
            videos_list.append(str(video['url']))
            count+=1
        if count == numofvideos:
            return videos_list

# Get list of live streams for a specific game on twitch (Ordered by highest viewer count)
def get_live_streams(game, numofstreams):
    livestreams = client.get_streams(game_ids=get_game_id(game))
    count = 0
    live_streams = []
    for stream in livestreams:
        if count < numofstreams:
            live_streams.append(str(stream['title'].capitalize() + ", " + stream['user_name'].capitalize()))
            count+=1
        if count == numofstreams:
            return live_streams

# Get follow-to-follow relationship between two streamers
def get_follow_relationship(streamer1, streamer2):
    info = client.get_user_follows(from_id=get_id(streamer1), to_id=get_id(streamer2))
    if len(info) != 0:
        return (streamer1.capitalize(), 'has a follow affiliation with', streamer2.capitalize())
    else:
        return (streamer1.capitalize(), 'has no follow affiliation with', streamer2.capitalize())