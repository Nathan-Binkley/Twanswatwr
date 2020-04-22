import os, time, random, json, datetime, io 
import tweepy
from gtts import gTTS
import keys

import sys


#SETTINGS

filterList = ['://','www.','.com','.net','.gov','.org','https','http', '@', '#', 'RT']

auth = tweepy.OAuthHandler(keys.API_KEY[0], keys.API_KEY[1])
auth.set_access_token(keys.ACCESS_TOKEN[0],keys.ACCESS_TOKEN[1])
word = tweepy.API(auth)

people_at = ['realDonaldTrump', 'JoeBiden', 'LindseyGrahamSC']
people_id = []
person = ['25073877']


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        whom = status.user.screen_name
        if whom in people_at:
            try:
                with io.open("OwO.json", "w", encoding='utf8') as f:
                    json.dump(status._json, f, indent=4)
                print("New Status ID: " + str(status.id))
                if hasattr(status, 'retweeted_status'):
                    tweet_id=status.retweeted_status.id
                    print("Retweeted Status ID: " + str(tweet_id))
                    #whom = status.retweeted_status.user.id
                    try:
                        tweet = status.retweeted_status.extended_tweet["full_text"]
                    except:
                        tweet = status.retweeted_status.text
                else:
                    tweet_id = status.id
                    try:
                        tweet = status.extended_tweet["full_text"]
                    except AttributeError:
                        tweet = status.text
                print(str(whom) + " just tweeted new ID: " + str(tweet_id))
                print("With Status: " + tweet)
                

                if whom in owo(tweet): #if retweet, don't @them as well
                    tweet = owo(tweet)
                else:
                    tweet = "@" + whom + " " + owo(tweet)

                print("Tweeting: " + tweet + "\n\n")
                Tweet(tweet, tweet_id)
                
            except Exception as e:
                print("Error, Unknown issue")
                print(e)
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


def owo(text):
    texts = text.split(" ")
    owod = ""
    for i in texts:
        i = i.rstrip()
        if i == '&amp;':
            owod += '&'
        else:
            temp = False
            for j in filterList: #allows filtering 
                if j in i:
                    owod += i
                    temp = True
                    break
            if not temp:
                for j in i:
                    if j == "l" or j == "r":
                        owod += "w"
                    elif j == "L" or j == "R":
                        owod += "W"
                    else:
                        owod += j
        owod += " "

    if len(owod) < 150:
        helper = random.randint(0,80)
        if helper < 10:
            owod += "owo "
        elif helper < 20 and helper >= 10:
            owod += "rawr XD "
        elif helper < 30 and helper >= 20:
            owod += "ouo "
        elif helper < 40 and helper >= 30:
            owod += "OwO *notices bulge* "
        elif helper < 50 and helper >= 40:
            owod += "Pwease Daddy? I can be youw pwincess (⑅˘꒳˘) " 
        elif helper < 60 and helper >= 50:
            owod += "º꒳º "
        elif helper < 70 and helper >= 60:
             owod += "*Kisses you from a distance because social distancing*"
        else:
            owod += "*nuzzles your body pillow because I cant because social distancing* OwO"

    return owod


def Tweet(text, resp_id):
    try:
        print("responding to " + str(resp_id))
        word.update_status(status=text, in_reply_to_status_id=resp_id)
        
    except Exception as e:
        print(e)
        if "[{'code': 185, 'message': 'User is over daily status update limit.'}]" in str(e):
            print("Sleeping for 2 seconds")
            time.sleep(2)
            Tweet(text,resp_id)
        elif "[{'code': 186, 'message': 'Tweet needs to be a bit shorter.'}]" in str(e):
            time.sleep(1)
            print("\n\nTweet not sent\nTrying again with 1 character shorter:")
            print("\nFailed Tweet: " + str(text))
            print("Length: " + str(len(text)))
            print("\nRetrying: " + text[:280])
            Tweet(text[:280],resp_id)
        else:
            print(e)       
    print("Tweet sent successfully")
        
            

def launch_stream():
    myStreamListener = MyStreamListener() 
    myStream = tweepy.Stream(auth = word.auth, listener=myStreamListener)
    myStream.filter(follow=people_id, is_async=False) #Best solution.


def getIDs(listOfPeopleAts):
    for i in listOfPeopleAts:
        response = word.user_timeline(id=i, count=1)
        people_id.append(str(response[0]._json['user']['id']))
        


def orig_owo(): #first solution, loops through the list every 10 seconds. Resulted in badness
    while True:
        # for i in people:
        whom = 'realDonaldTrump'
        i = whom
        
        response = word.user_timeline(id = whom , count = 1, tweet_mode='extended')
        if len(response) > 0:
            status = response[0]
            status = status._json
            text=""

            with open("Trumps.json", 'w') as f: #inspection of API response
                json.dump(status, f, indent=4)

            try:
                text = status['retweeted_status'] #if retweet
                text = text['full_text']
                tweet_id = status['retweeted_status']
                tweet_id = tweet_id['id']
            except:     
                text = status['full_text']
                tweet_id = status['id']
            
            twitter_at = status['user']['screen_name']

            # print(text)
            # print(owo(text))

            tweet = ''

            
        else:
            print("Returned Empty List")
            

        time.sleep(10)

# ----------------- READ IN FROM FILE IF NECESSARY --------------------- #
def in_files(name):
    filename = name #no ".txt" plz
    with open(filename + ".txt", "r") as f:
        text = f.read()

    with open(filename + "_owod.txt","w+") as f:
        f.write(owo(text))


# -------------------- UNCOMMENT FOR TEXT-TO-SPEECH -------------------------- #
def to_Speech(text):
    tts = gTTS(text=owo(text), lang='en')
    tts.save("owo.mp3") 
    
    #Playing the converted file (keys.wmfilepath = path to windows media player)
    os.system('start '+ keys.wmfilepath + ' ' + keys.mp3filepath + 'owo.mp3"')

# ------------------- MAIN CODE HERE --------------------------------#

getIDs(people_at)
# load_tweet_log()
while(True):
    try:      
        launch_stream()
    except Exception as e:
        print(e)
        time.sleep(120)
