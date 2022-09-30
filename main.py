import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kt
from sys import exit

MASTER = 'Sir'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

#speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will wish you as per the current time
def wishme():

    hour = int(datetime.datetime.now().hour)

    if hour >= 5 and hour <12:

        speak('Good Morning' + MASTER)

        now = datetime.datetime.now()
        day = now.strftime("%A")
        strTime = datetime.datetime.now().strftime("%H:%M")

        speak(f'Today the day is {day} and the time is {strTime}')


    elif hour>=12 and hour <18:

        speak('Good Afternoon' + MASTER)

        now = datetime.datetime.now()
        day = now.strftime("%A")
        strTime = datetime.datetime.now().strftime("%H:%M")

        speak(f'Today the day is {day} and the time is {strTime}')

    else:
        speak('Good Evening' + MASTER)

        now = datetime.datetime.now()
        day = now.strftime("%A")
        strTime = datetime.datetime.now().strftime("%H:%M")

        speak(f'Today the day is {day} and the time is {strTime}')

#this function will take command from the microphone
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        speak('Listening')
        audio = r.listen(source)

    try:

        speak('wait')
        query = r.recognize_google(audio, language = 'en-in')
        print(f'user said {query}')


    except Exception as e:

        print(f'user said {query}')
        query = None

    return query

#logic for executing tasks as per the query
def task():

    speak("Initializing Jarvis..........")
    wishme()
    i = 0
    while True:

        if i == 0:
            speak('What do you want me to do sir')

        if i != 0:
            speak('Do you want me todo anything else for you sir')
        i = + 1

        query = takecommand()
        print(query)

        if not query:
            speak('You Did not say anything...')

        elif 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak(results)

        elif 'close google' in query.lower():
            speak('Closing Google Chrome')
            os.system("killall -9 'Google Chrome'")

        elif 'open youtube' in query.lower():
            speak('Opening Youtube')
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open("https://www.youtube.com/")
            speak('Youtube Opened')

        elif 'open google' in query.lower():
            speak('Opening Google')
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open("https://www.google.com/")
            speak("Google Opened")

        elif 'open' and 'laptop'  in query.lower():

            query = query.lower().replace('open', '')
            query = query.lower().replace('hello', '')
            query = query.lower().replace('jarvis', '')
            query = query.lower().replace('laptop', '')
            query = query.lower().replace('on', '')
            query = query.lower().replace('my', '')
            query = query.lower().replace(' ', '')
            speak(f'Opening {query}')
            os.system(f"open /Applications/{query}.app")

        elif 'open' in query.lower():
            query = query.lower().replace('open', '')
            query = query.lower().replace('hello', '')
            query = query.lower().replace('jarvis', '')
            query = query.lower().replace(' ', '')
            speak(f"Opening {query}")
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(f"https://www.{query}.com/")
            speak(f'{query} Opened')

        elif 'search' and 'youtube' in query.lower():
            query = query.lower().replace('play', '')
            query = query.lower().replace('hello', '')
            query = query.lower().replace('jarvis', '')
            query = query.lower().replace('on youtube', '')
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            speak('showing the result of search on Youtube')
            webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + query+ "+")


        elif 'search' in query.lower():
            query = query.lower().replace('search','')
            query = query.lower().replace('hello', '')
            query = query.lower().replace('jarvis', '')
            query = query.lower().replace('on google', '')
            speak(f'Searching {query}')
            kt.search(query)
            speak("I have show you the result of your search")

        elif 'play' and 'youtube' in query.lower():
            query = query.lower().replace('play', '')
            query = query.lower().replace('hello', '')
            query = query.lower().replace('jarvis', '')
            query = query.lower().replace('on youtube', '')
            speak('Playing {query} on youtube')
            kt.playonyt(query)


        elif 'day' and 'today' in query.lower():
            now = datetime.datetime.now()
            day= now.strftime("%A")
            speak(f'{MASTER} the day is {day}')

        elif 'time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'{MASTER} the time is {strTime}')

        elif 'year' in query.lower():
            today = datetime.datetime.now()
            speak(f'{MASTER} the year is {today.year}')

        elif 'month' in query.lower():
            today = datetime.datetime.now()
            speak(f'{MASTER} the year is {today.month}')

        elif 'yourself' in query.lower():
            speak('Hello I am jarvis. I am a virtual Assistant. I can perform some basic task like opening application, searching and many more. I dont know much about my self yet. This is all i know at this moment')

        elif 'about me' in query.lower():
            speak('Hello Sir, Your Name is Fasih Muhammad Virk. You are 22 year old. You are 5 feet 4 inches tall.  Currently studying computer sciecne in institute of space technology. you are also my creater')

        elif 'favourite food' in query.lower():
            speak('You favourite Food is Briyani')

        elif 'favourite color' in  query.lower():
            speak('You favourite color is Black')

        elif 'my father' in query.lower():
            speak('you father name is Ilyas Saleem')

        elif 'my mother' in query.lower():
            speak('you mother name is Sidra Ilyas')

        elif 'how many' and 'sibling' in query.lower():
            speak('You have five siblings')
            speak('you have Two sister,.... Manoush and Zainab')
            speak( 'you have Three Brother,...... Masif, Ali and  Aounn')
            speak('You are the eldest')


        elif 'thank uou jarvis' in query.lower():
            speak('No problem sir')

        elif 'logout' in query.lower():
            exit(0)
        else:
            speak("sorry.. I don't know the answer sir")


print('Jarvis')

task()







