import os, time, random, json, datetime, io 
import tweepy
from gtts import gTTS
import keys

import sys




class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        whom = status.user.screen_name
        if whom in people_at:
        
            tweet_id = status.id
            print(whom + " just tweeted new ID: " + str(tweet_id))

            with io.open("Trumps2.json", "w", encoding='utf8') as f:
                json.dump(status._json, f, indent=4)

            if hasattr(status, 'retweeted_status'):
                try:
                    tweet = status.retweeted_status.extended_tweet["full_text"]
                except:
                    tweet = status.retweeted_status.text
            else:
                try:
                    tweet = status.extended_tweet["full_text"]
                except AttributeError:
                    tweet = status.text
            print("With Status: " + tweet)
            with io.open("Trumps2.txt", "a+", encoding='utf8') as f:
                f.write(whom + " just tweeted: " + tweet + "\n\n")   

            if whom in owo(tweet): #if retweet, don't @them as well
                tweet = owo(tweet)
            else:
                tweet = "@" + whom + " " + owo(tweet)

            # if len(tweet) > 280:
            #     tweet=tweet[:279]

            print("Tweeting: " + tweet + "\n\n")
            try:
                word.update_status(status=tweet, in_reply_to_status_id = tweet_id)
            except tweepy.TweepError:
                try:
                    word.update_status(status=tweet[:278], in_reply_to_status_id=tweet_id)
                except:
                    try:
                        word.update_status(status=tweet[:270], in_reply_to_status_id=tweet_id)
                    except:
                        word.update_status(status=tweet[:250] + "...", in_reply_to_status_id=tweet_id)
            except:
                print("Error, Unknown issue")
        
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
                    elif i == " ":
                        if random.randint(0,100) < 10:
                            helper = random.randint(0,60)
                            if helper < 10:
                                owod += " owo "
                            elif helper < 20 and helper >= 10:
                                owod += " XD "
                            elif helper < 30 and helper >= 20:
                                owod += " ouo "
                            elif helper < 40 and helper >= 30:
                                owod += " OwO *notices bulge* "
                            elif helper < 50 and helper >= 40:
                                owod += " rawr " 
                            else:
                                owod += " *nuzzles you* "
                        else:
                            owod += " "
                    else:
                        owod += j
        owod += " "

    if len(owod) < 150:
        helper = random.randint(0,60)
        if helper < 10:
            owod += "owo "
        elif helper < 20 and helper >= 10:
            owod += "XD "
        elif helper < 30 and helper >= 20:
            owod += "ouo "
        elif helper < 40 and helper >= 30:
            owod += "OwO *notices bulge* "
        elif helper < 50 and helper >= 40:
            owod += "rawr " 
        else:
            owod += "*nuzzles you* "
    return owod

# TODO: 
# Encapsulations
# Specific Tweepy.TweepError handling. Right now it's just general 

#SETTINGS

filterList = ['://','www.','.com','.net','.gov','.org','https','http', '@', '#', 'RT']

auth = tweepy.OAuthHandler(keys.API_KEY[0], keys.API_KEY[1])
auth.set_access_token(keys.ACCESS_TOKEN[0],keys.ACCESS_TOKEN[1])
word = tweepy.API(auth)

people_at = ['realDonaldTrump', 'ewarren', 'BernieSanders', 'JoeBiden', 'LindseyGrahamSC']#, 'Anon1Anti']
people_id = ['25073877', '357606935', '216776631', '939091','432895323']#,'1212229630691643392']
person = ['25073877']


def launch_stream():
    myStreamListener = MyStreamListener() 
    myStream = tweepy.Stream(auth = word.auth, listener=myStreamListener)
    myStream.filter(follow=people_id, is_async=False) #Best solution.


def getIDs(listOfPeopleAts):
    for i in listOfPeopleAts:
        response = word.user_timeline(id = i, count=1)
        print(response[0]._json['user']['id'])
        print(response[0]._json['user']['screen_name'])


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

            if tweet_id in keys.already_responded_ids:
                print("Already responded to this TweetID " + str(tweet_id) + " from " + str(i))
                tweeted = True
            else:
                tweeted=False
                keys.already_responded_ids[tweet_id] = text
                print("new Tweet ID " + str(tweet_id) + " from " + str(i))
                try:
                    with open("IDS.txt", "a+") as f:
                        f.write(str(tweet_id) + " " + text.strip() +  "\n")
                except: 
                    print("Can't write tweet")
                    with open("IDS.txt", "a+") as f:
                        f.write(str(tweet_id) + " Can't write tweet" +  "\n")

            if not tweeted:
                try:
                    
                    print("Tweeted:", tweet)
                    try:
                            
                        with open(i+'_log.txt', "a+") as f:
                            f.write(str(datetime.datetime.now()) + " " + text + "\n" + tweet + "\n\n")
                    except: 
                        print("Can't write tweet")
                        with open("IDS.txt", "a+") as f:
                            f.write(str(tweet_id) + " Can't write tweet" +  "\n")

                except tweepy.TweepError:
                    print("No new tweet from " + i + " at time " + str(datetime.datetime.now()))

                except:
                    with open(i+'_log.txt', "a+") as f:
                        f.write(str(datetime.datetime.now()) + " Cannot Write Tweet -- Not ASCII" + "\n\n")
                    print("writeError, not ASCII")
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

##Connect to DB
mydb = mysql.connector.connect(host = 'localhost', user=keys.DB_User, passwd=keys.DB_Pass)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

#launch_stream()