import pyttsx3
import speech_recognition as sr
import wikipedia as wiki
import webbrowser
import datetime
import os 

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[2].id)

def speak(answer):
    engine.say(answer)
    engine.runAndWait()
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening..')
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print('recognising..')
        audio=r.recognize(audio)
        print('user said:',audio)
    except: 
        revert='please say that again'
        print(revert)
        speak(revert)
        return 'None'
    return audio
def wish():
    time=datetime.datetime.now().hour
    if(time>=0 or time<12):
        speak('good morning sir')
    elif(time>=12 or time<4):
        speak('good afternoon sir')
    else: speak('good night sir')
    print(time)
wish()
speak('hello sir, this is your personal assistant')
speak('how can i help you')
while(True):
    query=take_command().lower()
    if('wikipedia' in query):
        speak('searching')
        query.replace('wikipedia',"")
        results=wiki.summary(query,sentences=2)
        speak('according to wikipedia')
        print(results)
        speak(results)
    elif('google' in query):
        webbrowser.open('google.com')
    elif('youtube' in query):
        webbrowser.open('youtube.com')
    # elif('insta' in query):
    #     from insta_automation import*
    # elif('amazon' in query):
    #     from amazon_automation import*
    elif('command' in query):
        os.system('start cmd')
    elif('calender' in query):
        webbrowser.open('calender.com')
    elif('time' in query):
        timenow=datetime.datetime.now()
        speak(f'time is {timenow}')
        print(timenow)
    if(query=='no thanks'):
        speak('Thank you for using me , have a great day')
        break
