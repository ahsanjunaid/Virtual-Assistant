    # Ahsan's Virtual Assistant
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import pyaudio

warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('\nSay Something!')
        audio = r.listen(source)
        data =' '
        try:
            data = r.recognize_google(audio)
            print('You Said: ' + data)
        except sr.UnknownValueError:
            print('Oops ! Couldnt Understand What You Said\nSystem by Ahsan Junaid')
        except sr.RequestError as e:
            print('Error ' + e)

        return data


def assistantResponse(text):

    print(text)
    myobj = gTTS(text=text,lang='en',slow=False)
    myobj.save('assistant_response.mp3')
    os.system('start assistant_response.mp3')


def activationWord(text):
    WAKE_WORDS = ['Hey Computer', 'Hi Computer', 'Okay Computer']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False


def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['Janusary', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + " " + month_names[monthNum-1] + ' the ' + ordinalNumbers[dayNum-1] + " accorrding to your system, bleep blop."


def greeting(text):

    GREETING_INPUTS = ['hi', 'hello', 'hey', 'holla', 'greetings', 'salam', 'wassup']
    GREETING_RESPONSES = ['Howdy!', 'Hey There!', 'Hi!']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + ' '

    return ''


def getPerson(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + '' + wordList[i+3]


while True:

    text = recordAudio()
    response = ' '
    if (activationWord(text) == True):
        response = response + greeting(text)

    if ('hi', 'hello', 'hey', 'holla', 'greetings', 'salam', 'wassup' in text):
        response = response + greeting(text)

    if ('date' in text):
            get_date = getDate()
            response = response + ' ' + getDate()

    if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

    if ('who made you' in text):
            response ="i was made by Ahsan Junaid"

    if ('time' in text):
        timenow = datetime.datetime.now()
        ampm = ''
        if timenow.hour >=12:
            ampm = 'p.m'
            hour = timenow.hour - 12
        else:
            ampm = 'a.m'
            hour = timenow.hour

        if timenow.minute<10:
            minute = '0' + str(timenow.minute)
        else:
            minute = str(timenow.minute
                             )
        response = response + ' ' + 'It Is ' + str(hour) + ':' + minute + ' ' + ampm + ', tick tok'

    assistantResponse(response)