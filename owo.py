import os, time, random
import tweepy
from gtts import gTTS
import keys

text=""




owod = ""

for i in text:
    i.lower()
    if i == "l" or i == "r":
        owod += "w"
    elif i == "L" or i == "R":
        owod += "W"
    # elif i == " ":
    #     if random.randint(0,100) < 10:
    #         helper = random.randint(0,60)
    #         if helper < 10:
    #             owod += " owo "
    #         elif helper < 20 and helper >= 10:
    #             owod += " XD "
    #         elif helper < 30 and helper >= 20:
    #             owod += " ouo "
    #         elif helper < 40 and helper >= 30:
    #             owod += " OwO *notices bulge* "
    #         elif helper < 50 and helper >= 40:
    #             owod += " rawr " 
    #         else:
    #             owod += " *nuzzles you* "
    #     else:
    #         owod += " "
    else:
        owod += i


auth = tweepy.OAuthHandler(keys.API_KEY[0], keys.API_KEY[1])
auth.set_access_token(keys.ACCESS_TOKEN[0],keys.ACCESS_TOKEN[1])
word = tweepy.API(auth)
word.update_status(status="HELLO WORLD")
print("Tweeted %s", "HELLO WORLD")

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