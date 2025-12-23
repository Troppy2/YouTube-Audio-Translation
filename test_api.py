import requests

url = "http://127.0.0.1:5000/translate"
data = {
    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "language": "en"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    # Save the audio file
    with open('translated_audio.mp3', 'wb') as f:
        f.write(response.content)
    print("Success! Audio file saved.")
else:
    print(f"Error: {response.status_code}")
    print(response.json())

    