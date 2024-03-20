import speech_recognition as sr
import os
import pyttsx3
import datetime
import time
import wikipedia
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import searching
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def recognize():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')

        print(f"User Said : {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again plaease")
        print("Say That again please")
        return "None"

    return query


def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am QuikAI. How may I help You")


if __name__ == "__main__":
    # welcome()
    if 1:
        query = recognize().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'help' in query:
            speak('No person in the world that can save you')
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = "C:/Users/a_moh/OneDrive/Desktop/movies/music"
            songs = os.listdir(music_dir)

            # print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:/Users/a_moh/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(codePath)
        elif 'open spotify' in query:
            spotify = 'C:/Users/a_moh/AppData/Roaming/Spotify/Spotify.exe'
            os.startfile(spotify)
        else:
            # if recognize()=="None":
            #     recognize()
            # else:
            query = query.replace(' ', '+')
            web = searching.website + query
            print(web)
            driver = webdriver.Chrome(service=Service(searching.path))
            driver.maximize_window()
            driver.get(web)
            time.sleep(100)
            driver.close()
