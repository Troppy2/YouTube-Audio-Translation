# Youtube-Audio-Translator

# Introduction 
While watching YouTube videos, I noticed that language barriers can make it difficult to access useful content. If you don’t understand the language being spoken, you’re unlikely to keep watching—and instead of finding the answer you were looking for, you might end up going down a rabbit hole searching for alternatives.This project was my attempt to solve that problem by creating a website that translates the audio in YouTube videos. Although I wasn’t able to complete it due to my limited experience with backend development and JavaScript, the idea remains something I’m passionate about improving in the future.


# Version 2 December 22, 2025
I added a back end to the code. The APIs I used for this program were Google's Transcript API, Google's Translate API, and Google's Text-to-Speech API. To link the back end to the front end, I used Flask. This new version has a couple of bugs. One I was able to find was that every time a URL was entered and a user pressed the translate button, the method for fetching the transcript wouldn't be able to fetch it. One main source of error that caused this when I was testing the backend was that the set_videoid function wasn't able to get the ID of the video the user would enter, which would always prompt the error message that the transcript wasn't available.
