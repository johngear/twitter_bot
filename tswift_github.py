import numpy as np 
import csv
import tweepy
print(tweepy.__version__)

class lyric_info:
    def __init__(self, album, song, lyric):
        self.album = album
        self.song = song
        self.lyric = lyric


full_struct = []

## format
## ['artist', 'album', 'track_title', 'track_n', 'lyric', 'line', 'year']

with open('/Users/johngearig/Desktop/fun_coding/taylor_swift_lyrics.csv', encoding = 'utf-8', errors='ignore') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    counter = 0
    for row in data:
        full_struct.append(lyric_info(row[1], row[2], row[4]))

#remove the first thing that just gives the definitions per columb
full_struct.pop(0)

def get_song(val):
    print(full_struct[val].album,"\n" ,full_struct[val].song,"\n" , full_struct[val].lyric, "\n\n")

def get_longer_lyric(val):

    #makes sure this won't overflow over the end of the list
    #also makes sure not have lyrics at the end of one song that also include next song
    if val< (len(full_struct)-5) and (full_struct[val].song == full_struct[val+3].song):
        print(full_struct[val].lyric +' '+ full_struct[val+1].lyric +' '+ full_struct[val+2].lyric +' '+ full_struct[val+3].lyric)
        print(full_struct[val].song)
    else:
        pass
        print('too close to end')

def get_num():
    total_length = 4862 ##this results from len(full_struct)
    return np.random.randint(total_length)

def return_longer_lyric(val):
    #makes sure this won't overflow over the end of the list
    #also makes sure not have lyrics at the end of one song that also include next song

    if val< (len(full_struct)-5) and (full_struct[val].song == full_struct[val+3].song):
        return( full_struct[val].lyric +' '+ full_struct[val+1].lyric +' '+ full_struct[val+2].lyric +' '+ full_struct[val+3].lyric)
        # print(full_struct[val].song)
    else:
        # pass
        return None

def return_song(val):
    return full_struct[val].song


# get_song(np.random.randint(len(full_struct)))
# get_song(np.random.randint(len(full_struct)))
# get_song(np.random.randint(len(full_struct)))

# for _ in range(20):
#     val = get_num()
#     get_longer_lyric(val)
#     print('\n')


#tweet now

api_key = "mind your own business"
api_secret_key = "mind your own business"

bearer_token = "mind your own business"

access_token = "mind your own business"
access_token_secret = "mind your own business"


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# api.update_status("Test tweet from Tweepy Python")

num_tweets = 1 
for _ in range(num_tweets):
    val = get_num()
    words = return_longer_lyric(val) 
    if words != None:
        tweet = api.update_status(words)
        api.update_status(status=return_song(val), in_reply_to_status_id=tweet.id_str)

    # print('\n')


#delete all the tweets from the twitter account with this 
# for status in api.user_timeline():
#     api.destroy_status(status.id)

##this is how to schedule the thing
#need to add this to the VIM file that opens when you type
# crontab -e
# 15 */3 * * * /opt/anaconda3/bin/python /Users/johngearig/Desktop/fun_coding/fuck_around.py