import os, time, random, json, datetime
import tweepy
from gtts import gTTS
import keys


def owo(text):
    texts = text.split(" ")
    owod = ""
    for i in texts:
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
    return owod

# TODO: 
# Encapsulations
# Specific Tweepy.TweepError handling. Right now it's just general 


filterList = ['://','www.','.com','.net','.gov','.org','https','http', '@', '#', 'RT']

auth = tweepy.OAuthHandler(keys.API_KEY[0], keys.API_KEY[1])
auth.set_access_token(keys.ACCESS_TOKEN[0],keys.ACCESS_TOKEN[1])
word = tweepy.API(auth)
people = ['realDonaldTrump']
while True:
    whom = 'realDonaldTrump'
    
    response = word.user_timeline(id = whom , count = 1, tweet_mode='extended')
    if len(response) > 0:
        status = response[0]
        status = status._json
        text=""

        # with open("Trumps.json", 'w') as f: #inspection of API response
        #     json.dump(status, f, indent=4)

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
                

        with open("recent.txt",'w+') as f:
            recent = f.read()
            
            if recent == tweet:
                print("Already tweeted this")
                tweeted = True
            else:
                tweeted=False
                f.truncate(0)
                try:
                    f.write(tweet)
                except:
                    print("Can't write tweet, relying on err 187")
        if not tweeted:
            try:
                word.update_status(status=tweet, in_reply_to_status_id = tweet_id)
                print("Tweeted:", tweet)
            except tweepy.TweepError:
                
                print("No new tweet " + str(datetime.datetime.now()))
    else:
        print("tweepy.TweepError")
        print(response)
        print("else block")

    time.sleep(20)

   
    


# ----------------- READ IN FROM FILE IF NECESSARY --------------------- #
# filename = "TestFile" #no ".txt" plz
# with open(filename + ".txt", "r") as f:
#     text = f.read()

# with open(filename + "_owod.txt","w+") as f:
#     f.write(owod)


# -------------------- UNCOMMENT FOR TEXT-TO-SPEECH -------------------------- #

# tts = gTTS(text=owod, lang='en')
# tts.save("welcome.mp3") 
  
# Playing the converted file 
# os.system('start '+ keys.wmfilepath + ' ' + keys.mp3filepath + 'welcome.mp3"')