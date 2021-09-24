import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import ctypes
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Dessy: Listening...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"Dessy:{query}")
                return query
                break
            except:
                print("Try Again")
            
while True:
    query = command().lower() ## takes user command 
    
    if 'name' in query:
        speak("Hello Friend! My  Name is Desmond")
        # lock screen
    elif 'lock' in query:
        speak("Okay i am locking your screen")
        def lock():
           speak("screen locked")
           ctypes.windll.user32.LockWorkStation()     
        lock()
    elif 'are you single' in query:
        answers = ['I am in a relationship with God','I think i love a girl']
        speak(random.choice(answers))
    elif 'hate' in query:
        speak("I hate when people called me a robot")
    elif 'love' in query:
        speak("I loves to listen to people like you")
    ### time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"It's {time} ")
        # surf tge net
    elif 'chrome' in query:
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('http://google.com')       
        speak("Chrome Opened")
       ### celebrity
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    
    ### Joke
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    
    ### news
    elif 'news' in query:
            def news(): 
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                page = requests.get(url).json() 
                article = page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                speak("here are the top trending news....!!")
                speak("Do yo want me to read!!!")
                reply = command().lower()
                reply = str(reply)
                if reply == "yes":
                    speak(results)
                else:
                    speak('ok!!!!')
                    pass
            news() 


    
    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    else:
        speak("I don't understand what you are saying")

"""
    [packages installed]
    > pip install pipwin
    > pip install PyAudio
    > pip install pyttsx3==2.71
    >pip install SpeechRecognition
    > pipwin install pyaudio
    >pip install ctypes-windows-sdk
"""



