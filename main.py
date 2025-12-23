from flask import Flask, request, jsonify, send_file
import os
from audiotranslate import AudioTranslate
from flask_cors import CORS
# Create Flask app instance
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return "Youtube Translator API is running"

@app.route('/translate', methods=['POST'])
def translate_video():
    try:
        # Get data from request
        data = request.get_json()
        youtube_url = data.get('url')
        target_language = data.get('language', 'en')
        
        # Check for yt url
        if not youtube_url:
            return jsonify({'Error': 'YouTube URL is required'}), 400
        
        # Create AudioTranslate instance
        translator = AudioTranslate(videoid='', lang=target_language)
        
        # Extract video ID from URL
        video_id = translator.set_videoid(youtube_url)
        if not video_id:
            return jsonify({'Error': 'Invalid YouTube URL'}), 400
        
        print(f"Video ID: {video_id}")  # Debug output
        
        # Get transcript
        transcript = translator.get_transcript()
        if not transcript:
            return jsonify({'Error': 'Failed to get transcript - video may not have captions'}), 500
        
        print(f"Got transcript, length: {len(transcript)}")  # Debug output
        
        # Translate
        translated = translator.translate_text()
        if not translated:
            return jsonify({'Error': 'Failed to translate text'}), 500
        
        print(f"Translation complete")  # Debug output
        
        # Convert to speech
        audio_filename = translator.text_to_speech(filename='translated_audio.mp3')
        if not audio_filename:
            return jsonify({'Error': 'Failed to convert to speech'}), 500
        
        print(f"Audio file created: {audio_filename}")  # Debug output
        
        # Send the audio file back to the user
        return send_file(audio_filename, as_attachment=True, download_name='translated_audio.mp3')
        if not os.path.exists(audio_filename):
            return jsonify({'error': 'Audio file was not created'}), 500
        response = send_file(audio_filename, as_attachment=True, download_name='translated_audio.mp3')
        try:
            os.remove(audio_filename)
        except Exception as e:
            print(f"An unknow error occured when removing file {e}")
            return None
    except Exception as e:
        print(f"Exception occurred: {str(e)}")  # Debug output
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)