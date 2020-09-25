import os, time, random, json, datetime, io, re 
import tweepy
from gtts import gTTS
import keys

from apscheduler.schedulers.blocking import BlockingScheduler

import sys

from bs4 import BeautifulSoup
from html import unescape


#SETTINGS

filterList = ['://','www.','.com','.net','.gov','.org','https','http', '@', '#', 'RT']
customEndings = ['( ͡° ͜ʖ ͡°) ',"*nuzzles you* OwO ", "*Pounces on Daddy's lap* UwU What's this? ",  "*stares deep into your eyes* I wuv you ", "*Kisses you* ", "º꒳º ", "Pwease Daddy? I can be youw pwincess (⑅˘꒳˘) " ,"OwO *notices bulge* ", "ouo ", "rawr XD ", "owo ", "UwU ", "*Softly pets your cute head* ", "Do you need some nuzzle wuzzle?"]
customBeginnings = ['Mommy ', '*Stares into your eyes and says* ', '( ͡° ͜ʖ ͡°) ', '*purrs on your lap* ', '*Jumps on Daddy\'s lap* ']
auth = tweepy.OAuthHandler(keys.API_KEY[0], keys.API_KEY[1])
auth.set_access_token(keys.ACCESS_TOKEN[0],keys.ACCESS_TOKEN[1])
word = tweepy.API(auth)

people_at = ['realDonaldTrump', 'JoeBiden', 'LindseyGrahamSC', 'HelpMeDebugOwO'] 
people_id = []
person = ['25073877'] #realDonaldTrump for test purposes
debug = ['1235370767048740864']

tweets = {}


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        whom = status.user.screen_name
        print(whom)
        if whom in people_at:
            try:
                with io.open("OwO.json", "w", encoding='utf8') as f:
                    json.dump(status._json, f, indent=4)
                print("New Status ID: " + str(status.id))
                if hasattr(status, 'retweeted_status'):
                    print(status.retweeted_status)
                else:
                    tweet_id = status.id
                    try:
                        tweet = status.extended_tweet["full_text"]
                    except AttributeError:
                        tweet = status.text
                    
                    print(str(whom) + " just tweeted new ID: " + str(tweet_id)) 

                    logTweet(tweet, whom, tweet_id)

                    print("With Status: " + tweet)

                    tweet = owo(tweet)
                    tweet = re.sub(r'\&\w*;', '&', tweet)
                    tweet = tweet.replace('@','')

                    print("Tweeting: " + tweet + "\n\n")
                    Tweet(tweet, tweet_id)
                
            except Exception as e:
                print("Error, Unknown issue")
                print(e)
        
    def on_error(self, status_code):
        print("ERROR")
        print(status_code)
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


def owo(text):
    owod = ""
    example = ''

    texts = text.split(" ") #Split on spaces
    for i in texts: #for each item in the split list
        i = i.rstrip()  #remove \n characters 
    
        temp = False 
        for j in filterList: #allows filtering based on predetermined list
            if j in i:  # if filter index in the original word
                owod += i   #ignore it
                temp = True
                break
        if not temp:    # if filter index not in word
            for j in i: # go through each letter
                if j == "l" or j == "r":    # replace
                    owod += "w"
                elif j == "L" or j == "R": # replace
                    owod += "W"
                else:
                    owod += j #add if no replace (not r or l)
        owod += " "

    if len(owod) < 150: # add custom beginning
        try:
            helper = random.randint(0,len(customBeginnings)-1)
            owod = customBeginnings[helper] + owod
        except:
            pass

    if len(owod) < 150: # add custom ending
        try:
            helper = random.randint(0,len(customEndings)-1)
            owod += customEndings[helper]
        except:
            pass

    return owod


def Tweet(text, resp_id):
    try:
        print("responding to " + str(resp_id))
        word.update_status(status=text, in_reply_to_status_id=resp_id, auto_populate_reply_metadata='true')
        print("Tweet sent successfully\n")
        time.sleep(10)
        
    except Exception as e:
        print(e)
        if "[{'code': 185, 'message': 'User is over daily status update limit.'}]" in str(e):
            print("Sleeping for 2 seconds")
            time.sleep(2)
            Tweet(text,resp_id)
        elif "[{'code': 186, 'message': 'Tweet needs to be a bit shorter.'}]" in str(e):
            time.sleep(1)
            print("\n\nTweet not sent\nTrying again with 1 character shorter:")
            Tweet(text[:len(text)-1],resp_id)
        else:
            print(e)       

def launch_stream():
    myStreamListener = MyStreamListener() 
    
    myStream = tweepy.Stream(auth = word.auth, listener=myStreamListener)
    myStream.filter(follow=debug, is_async=False) #Best solution.

def getIDs(listOfPeopleAts):
    for i in listOfPeopleAts:
        response = word.user_timeline(id=i, count=1)
        people_id.append(str(response[0]._json['user']['id']))
    print(people_at)
    print(people_id)

# Name = Twitter ID <Str>
# text = Twitter status <Str>
def logTweet(Text,Name, ID):
    words = Text.split()
    for i in range(len(words)):
        words[i] = words[i].rstrip()
    Text = " ".join(words)
    DT = datetime.datetime.now().replace(microsecond=0)
    try:
        if not os.path.isfile(f"logs/{Name}.txt"):
            with open(f'logs/{Name}.txt', 'w') as f:
                f.write("\n")
        with io.open("logs/"+str(Name)+".txt", "a+",  encoding="utf-8") as f:
            string = str(DT.isoformat().replace("T"," ")) + " " + str(ID) + " " + str(Text) + "\n"
            f.write(str(string))
        print("Successfully logged tweet")
    except Exception as e:
        print(e)

def orig_owo(): #first solution, loops through the list every 10 seconds. Resulted in badness

    # for i in people:
    whom = ['realDonaldTrump', 'JoeBiden', 'LindseyGrahamSC', 'HelpMeDebugOwO']
    for i in whom:
    
        response = word.user_timeline(id = i, count = 1, tweet_mode='extended')
        if len(response) > 0:
            status = response[0]
            status = status._json
            text=""

            with open("Trumps.json", 'w+') as f: #inspection of API response
                json.dump(status, f, indent=4)
            print(status.text)
            try:
                text = status['retweeted_status'] #if retweet
                text = text['full_text']
                print(text)
                tweet_id = status['retweeted_status']
                tweet_id = tweet_id['id']
            except:     
                text = status['full_text']
                tweet_id = status['id']
                print(text)
            
            twitter_at = status['user']['screen_name']
            tweet = ''
        else:
            print("Returned Empty List")
                
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

# load_tweet_log()
getIDs(people_at)
        
while(True):
    try:      
        launch_stream()
    except TimeoutError:
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(120)
