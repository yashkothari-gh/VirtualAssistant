import pyttsx3
from   pyttsx3.drivers import sapi5
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import pyjokes
import os
import pyautogui
import random
import json
from   urllib.request import urlopen
import requests
import wolframalpha
import time

engine = pyttsx3.init()

wolframalpha_app_id ='WJEW7U-G7A99KPWWY'

def speak(audio1):
    engine.say(audio1)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    Year=datetime.datetime.now().year
    Month=datetime.datetime.now().month
    Date=datetime.datetime.now().day
    speak("The date today is")
    speak(Date)
    speak(Month)
    speak(Year)

def wishme():
    speak('Hello Yash')
   
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<16:
        speak('Good Afternoon')
    elif hour>=16 and hour<20:
        speak('Good Evening')
    else:
        speak('Good Night')
    
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio,language="en-US")
        print(query)
    except Exception as e:
        print(e)
        print('Say that again please....')
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yashkothari3390@gmail.com','salmankhan@0')
    server.sendmail('yashkothari3390@gmail.com',to,content)
    server.close()

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img =pyautogui.screenshot()
    img.save('C:/Python36/screenshot.png')

if __name__ == "__main__":
    wishme()
    while True:
        speak('KotBot at your service .')
        speak('How can I help you sir') 
        query=TakeCommand().lower()
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'send mail'  in query:
            try:
                speak("What should I say?")
                content=TakeCommand()
                speak("Who is the receiver.Please enter the receriver below")
                receiver=input("Enter destination mail id : ")
                to=receiver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('Unable to send email')

        
        elif 'search in chrome' in query :
            speak('What should I search?')
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        

        elif 'youtube' in query:
            speak('What should I search on youtube?')
            search1=TakeCommand().lower()
            speak('Redirecting to youtube')
            wb.open('https://www.youtube.com/results?search_query='+search1)
        

        elif 'google' in query:
            speak('What should I search on google?')
            search1=TakeCommand().lower()
            speak('Searching')
            wb.open('https://www.google.com/search?q='+search1)
        

        elif 'joke' in query:
            speak('Sir,Here is your joke')
            joke()
        

        elif 'write a note' in query:
            speak('What should i write ,Sir')
            notes=TakeCommand()
            file = open('notes.txt','w')
            speak('Should I include date and time')
            ans=TakeCommand().lower()
            if 'yes' in ans or 'sure' in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes')
            else:
                file.write(notes)
                speak('Done taking notes')


        elif 'show note' in query:
            speak('Showing notes')
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())


        elif 'screenshot' in query:
            speak('Screenshot saved .')
            screenshot()


        elif 'play music' in query:
            songs_dir='C:/Users/yash/Music/New folder'
            music =os.listdir(songs_dir)
            speak('What should I play,Select a number')
            ans =TakeCommand().lower()
            while 'number' not in ans or ans!='random' or ans!='you choose':
                speak('Could not recognize you.Try Agaih!!')
                ans=TakeCommand().lower()
            if 'number' in ans:
                no =int(ans.replace('number',''))
            elif 'you choose' in ans or 'random' in ans:
                no=random.randint(1,10)


            os.startfile(os.path.join(songs_dir,music[no]))


        elif 'remember this' in query:
            speak('What do you want to remember')
            memory=TakeCommand()
            speak('You asked me to remember'+memory)
            remember =open('memory.txt','a')
            remember.write(memory)
            remember.close()


        elif 'do you remember something' in query:
            remember =open('memory.txt','r')
            speak('You asked me to remember the following thing , ....'+remember.read())


        elif 'give some news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&apiKey=f638fc9e5d094d4785faac061cdb27a5")
                data=json.load(jsonObj)
                i=1
                speak('Here are the top headlines')
                print('==========Headlines==========\n')
                for item in data['articles']:
                    if(i!=6):
                        
                        print(str(i)+'. '+item['title']+'\n')
                        print(item['description']+'\n')
                        speak(item['title'])
                        i+=1
            except Exception as e:
                print(str(e))


        elif 'where is' in query:
            query=query.replace('where is','')
            location=query
            speak('You asked to locate'+location)
            speak('Here is your location')
            wb.open_new_tab('https://www.google.com/maps/place/'+location)


        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            indx=query.lower().split().index('calculate')
            query=query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The answer is'+answer)
            speak('The answer is'+answer)


        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            res=client.query(query)
            try:
                ans=next(res.results).text
                print(ans)
                speak(ans)
            except StopIteration:
                print('No results')
                speak('No results,Sir.')


        elif 'stop listening' in query:
            speak('For how many seconds do you want me to sleep')
            ans =int(TakeCommand())
            time.sleep(ans)
            print('I am back online ,Sir.')


        elif 'go offline' in query:
            speak('Byee ,sir,Going offline.')
            exit()

        else:
            speak('Retry again in a few minutes')


       
    







