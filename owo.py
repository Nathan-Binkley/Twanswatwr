import os, time, random
from gtts import gTTS
import keys

text=""

filename = "TestFile" #no ".txt" plz

with open(filename + ".txt", "r") as f:
    text = f.read()

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

with open(filename + "_owod.txt","w+") as f:
    f.write(owod)

tts = gTTS(text=owod, lang='en')
tts.save("welcome.mp3") 
  
# Playing the converted file 
os.system('start '+ keys.wmfilepath + ' ' + keys.mp3filepath + 'welcome.mp3"')