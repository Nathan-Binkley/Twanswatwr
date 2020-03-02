# Twanswatwr
Translates standard text into owo-ified text.

# Summary

This project has grown so much and I'm very proud of the work I put into it. It has turned into a really cool project that is teaching me a *lot* about APIs, Customer behavior (Specifically on Twitter with other User's responses), and text engines.

# The Beginnings

This entire thing started out as a prank. I wanted to be able to duplicate files, change all of their contents to be "owo"-ified while keeping things safe and secure. The only issue would be storage space and that was fine. Pretty harmless if used in a proper sense. 

I gained large amounts of motivation and ideas from the community that surrounds me here at Clemson. My friend made a system that uses TTS to read "Moby Dick" in a low volume to whomever he launched the program on. This was brilliant. I figured I just wanted to owo something, as a joke. I made a very simple owo algorithm that basically just converts "l" and "r" within text to "w". I have plans to expand this somewhat soon, but because of the limitations of the current outsource (Twitter), I feel it might break things involving length sometimes and we want to avoid that.

At this point, I made my first owo. I made Moby Dick, but I owod it. It was extremely simple. The whole thing took maybe a few minutes. I knew this was just the beginning.

# The Middles

I began to take more motivation from other's projects. I showed my friends the night I did Moby Dick. Some of them, embarassingly (self described), understood it. They were mortified but excited enough to suggest other works that I should "owo." Being the entertainer that I am, I took it to another step. I integrated Google's Text To Speech engine. Turns out, it's really really bad at interpreting non-native words. Especially words that aren't really words. All caps words (such as MOBY DICK in the title of the text) were read letter by letter as an acronym. Words that it didn't know how to pronounce them were treated as a 4th grader treats a large SAT word. It spelled it out. Google's smart, but it's text to speech engine still feels like a 2nd grader just went and took their first SAT. This still wasn't good enough. While humorous when the speech was working, I found the process to be slow. 

Then, I remembered I had a Twitter account.

My first instinct was to think about what to do. Within a few days, I had it. Owo. Trump's. Tweets. Regardless of political standing this was one of my best ideas. I applied for a Twitter Developer API access key that same night. 

My rationale is pretty simple. Nobody takes anything more serious than followers of politicians on Twitter. Their followers generally treat the words of these people as if they're the word of whatever spirit you may believe in. These people were the perfect target for a harmless practical joke and it was a journey.

My first solution involved pinging the API every 10 seconds for everyone's most recent tweet. Not only was this not fast enough, it also resulted in me overloading the 150req/15min limit that Twitter has. This obviously wasn't working.

I swapped this out with the Streaming API where it currently sits.

# The Current State of things

Currently The system works on my laptop. I have to re-launch it every time I shut it. My colleagues keep telling me I should upload it to AWS Lambda, which honestly might be a good idea.

I also want to take the data and put it in a database. 