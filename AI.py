import pyttsx3
import wikipedia
import os 
import datetime
import webbrowser
aisay = pyttsx3.init('sapi5')
voices = aisay.getProperty('voices')
print(voices[1].id)
aisay.setProperty('voice', voices[1].id)
def speak(audio):
    aisay.say(audio)
    aisay.runAndWait()
speak('HELLO THERE IS THERE SOMETHING I CAN HELP YOU WITH?')
userAsk = True
while userAsk == True:
    words = input('Enter some work to do: ')
    words = words.lower()
    if 'google' in words:
        speak(' Launching google in 3 2 1')
        webbrowser.open('https://google.com')
    elif 'youtube' in words:
        speak('Launching youtube in 3 2 1')
        webbrowser.open('https://youtube.com')
    elif 'facebook' in words:
        speak('Launching facebook in 3 2 1')
        webbrowser.open('https://facebook.com')
    elif 'github' in words:
        speak('Launching github in 3 2 1')
        webbrowser.open('https://github.com')
    elif 'what can you do' in words:
        speak('I am a program design to help you to do your different browers/personal tasks')
    elif 'delete' in words:
        speak('Commanded to Delete myself. Deleting Myself in 3 2 1  ')
        os.remove('AI.py')
    elif 'wikipedia' in words:
        speak('Searching on wikipedia please stand by & be patience')
        words = words.replace('wikipedia', '')
        resultshow = wikipedia.summary(words, sentences = 3)
        print(resultshow)
        speak(resultshow)
    elif 'are you an ai' in words:
        speak('I am a software developed by Nile Sunar ')
    elif 'hello' in words:
        speak('Oh Hello There nice to meet and greet you :)')
    elif 'time' in words:
        speak(f'The hour is {datetime.datetime.now().hour} HOURS and the full date is {datetime.datetime.now()} ')
    elif 'quit' in words:
        speak('Are you sure you want to quit this program? y/n')
        user = input('')
        if user == 'y':
            quit()
        else:
            True
    else:
        speak("I didn't get that. Is there Something I can help you with?") 