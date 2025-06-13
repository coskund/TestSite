from gtts import gTTS

# List of entries with name and text
entries = [
    {"name": "million", "text": "million trash found"},
    {"name": "enemy", "text": "found potential enemy"},
    {"name": "danger", "text": "you are under attack"},
    {"name": "problem", "text": "there is a problem"}
]

# Loop through each entry and create MP3
for entry in entries:
    tts = gTTS(entry["text"], lang='en')
    filename = f"{entry['name']}.mp3"
    tts.save(filename)
    print(f"Saved: {filename}")
