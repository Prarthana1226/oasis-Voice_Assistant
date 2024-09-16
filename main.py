import pyttsx3 as p
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import webbrowser
from selenium_web import *
from YT_auto import *
import randfacts
from jokes import *

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("hello prarthna, i am your voice assistant riva. how are you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("i am also having a great day maam")
speak("what can i do for you ?")




with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)


if "information" in text2:
    speak("You need information related to which topic ?")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor))
    assist = Infow()
    assist.get_info(infor)

elif "time" in text2:
    time=datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    engine.say(time)
    engine.runAndWait()

elif "date" in text2:
    to_date=datetime.datetime.now()
    print(to_date)
    engine.say("today is "+to_date.strftime("%d") + "of" + to_date.strftime("%B"))
    engine.runAndWait()

elif "play" and "video" in text2:
    speak("You want to play which video ?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))
    assist = YouTubeAutomation()
    assist.open_youtube()
    assist.search_video(vid)
    assist.click_first_video()
    assist.close_browser()

elif "fact" in text2:
    speak("Sure maam, ")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)

elif "joke" in text2:
    speak("Sure maam, get ready for some chuckles")
    ar=joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])