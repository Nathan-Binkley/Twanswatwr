import os, time, random, json, datetime
import tweepy
from gtts import gTTS
import keys

import sys



class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.user.screen_name == 'realDonaldTrump':
            print(status.full_text)
            return False
        print(status.user.screen_name)
        

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


def owo(text):
    texts = text.split(" ")
    owod = ""
    for i in texts:
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


filterList = ['://','www.','.com','.net','.gov','.org','https','http', '@', '#', 'RT']

auth = tweepy.OAuthHandler(keys.API_KEY[0], keys.API_KEY[1])
auth.set_access_token(keys.ACCESS_TOKEN[0],keys.ACCESS_TOKEN[1])
word = tweepy.API(auth)

people_at = ['realDonaldTrump', 'ewarren', 'BernieSanders', 'JoeBiden', 'AOC', 'LindseyGrahamSC']
people_id = ['25073877', '1230694420078567424', '1230685093850701825', '1230685572714418176', '1230697952240291844','1230613975290740736']
person = ['25073877']
processingQueue = []

myStreamListener = MyStreamListener() 
myStream = tweepy.Stream(auth = word.auth, listener=myStreamListener)
myStream.filter(follow=person, is_async=False)

'''
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

        if whom in owo(text): #if retweet, don't @them as well
            tweet = owo(text)
            if len(tweet) >= 140:
                tweet=tweet[280:]
                
        else:
            tweet = "@" + twitter_at + " " + owo(text)
            
            if len(tweet) >= 280:
                tweet=tweet[:280]
                

        
        if tweet_id in keys.already_responded_ids:
            print("Already responded to this TweetID " + str(tweet_id) + " from " + str(i))
            tweeted = True
        else:
            tweeted=False
            keys.already_responded_ids[tweet_id] = text
            print("new Tweet ID " + str(tweet_id) + " from " + str(i))
            try:
                with open("IDS.txt", "a+") as f:
                    f.write(str(tweet_id) + " " + text +  "\n")
            except: 
                print("Can't write tweet")
                with open("IDS.txt", "a+") as f:
                    f.write(str(tweet_id) + " Can't write tweet" +  "\n")

        if not tweeted:
            try:
                word.update_status(status=tweet, in_reply_to_status_id = tweet_id)
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

'''
    


# ----------------- READ IN FROM FILE IF NECESSARY --------------------- #
# filename = "TestFile" #no ".txt" plz
# with open(filename + ".txt", "r") as f:
#     text = f.read()

# with open(filename + "_owod.txt","w+") as f:
#     f.write(owod)


# -------------------- UNCOMMENT FOR TEXT-TO-SPEECH -------------------------- #

# tts = gTTS(text=owo(tweet), lang='en')
# tts.save("welcome.mp3") 
  
# Playing the converted file 
# os.system('start '+ keys.wmfilepath + ' ' + keys.mp3filepath + 'welcome.mp3"')