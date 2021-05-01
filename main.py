def speak(text):
    from playsound import playsound
    from gtts import gTTS
    tts = gTTS(text=text, lang='en', tld='co.in')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound(filename)


inp = str(input("Enter What You Want Speak And Save The File:"))

speak(inp)
