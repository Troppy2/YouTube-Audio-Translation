"""
Notes for myself:

    from youtube_transcript_api import YouTubeTranscriptApi

    video_id = "VIDEO_ID"  # Replace with your video ID
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

    # transcript_list is a list of dictionaries containing text and timestamps
    for item in transcript_list:
        print(item['text'])
        pip install youtube-transcript-api
        pip install googletrans==4.0.0rc1
        pip install gtts
        pip install flask
"""
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask
from googletrans import Translator
from gtts import gTTS

class AudioTranslate:  # class to get, details of the video, text, id, and lang
    def __init__(self, videoid, lang):  # constructor class that gets required data for other objects
        self.videoid = videoid
        self.lang = lang
        self.original_text = None  # Store original transcript
        self.translated_text = None  # Store translated text
    
    def set_lang(self, lang):  # setter func for lang
        self.lang = lang

    def set_videoid(self, url):  # setter for vidID
        if "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1].split("?")[0].split("&")[0]
        elif "v=" in url:
            video_id = url.split("v=")[1].split("&")[0]
        else:
            return None
        self.videoid = video_id
        return self.videoid
    
    def get_transcript(self):  # func for full text -- Theres a bug in this function either nothing goes into the text or something wrong is happening here
        try:
            transcript = YouTubeTranscriptApi.get_transcript(self.videoid)
            full_text = ""
            for segment in transcript:
                full_text += segment['text'] + " "
            self.original_text = full_text  # Store in original_text, not translate_text
            return full_text
        except Exception as e:
            print(f"Transcript error: {e}")
            return None
    
    def translate_text(self):
        try:
            translator = Translator()
            result = translator.translate(self.original_text, dest=self.lang)
            self.translated_text = result.text  # Store the translated result
            return self.translated_text  # Return it
        except Exception as e:
            print(f"Translation error: {e}")
            return None
    
    def text_to_speech(self, filename='output.mp3'):
        try:
            tts = gTTS(text=self.translated_text, lang=self.lang)  # Use translated_text
            tts.save(filename)
            return filename
        except Exception as e:
            print(f"Text-Speech Error: {e}")
            return None
    
    # After translation
    def process_video(self, filename='translated_audio.mp3'):
        # Complete pipeline method
        if self.get_transcript() is None:
            return None
        if self.translate_text() is None:
            return None
        return self.text_to_speech(filename)