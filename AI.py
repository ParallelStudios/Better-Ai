from ast import main
from asyncio.windows_events import NULL
from asyncore import write
from datetime import datetime
from email.mime import application
from logging.config import listen
from math import fabs
from re import search
from unittest import result
from urllib import response
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3
import sys
import webbrowser
import wikipedia
import wolframalpha
import googlesearch
import pyautogui

recognizer = speech_recognition.Recognizer()
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
speaker = pyttsx3.init()
with open('recorded_name.txt', 'r+') as f:
   name = f.read()
   
todo_list = ['Shower', 'Do homework', 'Work on the game']
if name != "":
    speaker.say(f'Welcome {name}!')
else:
    speaker.say("Welcome")
def create_note():
    global recognizer
    
    speaker.say("What do you want your note to say sir?")
    print("Say note")
    speaker.runAndWait()
    
    done = False

    while done == False:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
                audio = recognizer.listen(mic) 
                
                note = recognizer.recognize_google(audio, language='en_gb')
                note = note.lower()
                
                speaker.say("Choose a filename!")
                print("choose a file name")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
                audio = recognizer.listen(mic)
                
                filename = recognizer.recognize_google(audio, language='en_gb')
                filename = filename.lower()
                
            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done = True
                speaker.say("Note recorded")
                print("note")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not quite catch that. Please try again")
            speaker.runAndWait()
            
            
def add_todo():
    global recognizer
    
    speaker.say("What would you like to add to your to do list")
    speaker.runAndWait()
    
    done = False
    
    while not done:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                item = recognizer.recognize_google(audio, language='en_gb')
                item = item.lower()
                
                todo_list.append(item)
                done = True
                
                speaker.say(f"I added {item} to your to do list sir!")
                speaker.runAndWait
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not quite catch that. Please try again sir!")
            speaker.runAndWait()
            
            
def show_todos():
    
    speaker.say("The items on your to do list are the following, ")
    for item in todo_list:
        speaker.say(item)
        speaker.runAndWait()
        
def write_name():
    global recognizer
    
    speaker.say("Say your name")
    print("Say name")
    speaker.runAndWait()
    
    done = False

    while done == False:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
                audio = recognizer.listen(mic)
            
                name = recognizer.recognize_google(audio, language='en_gb')
                name = name.lower()
                
            with open("recorded_name.txt", 'w') as f:
                f.write(name)
                done = True
                speaker.say("Name written")
                print("name")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not quite catch that. Please try again")
            speaker.runAndWait()
            
def searching_the_web():
    global recognizer
    
    speaker.say("what would you like to search")
    speaker.runAndWait()
    
    done = False

    while done == False:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
                audio = recognizer.listen(mic)
            
                search = recognizer.recognize_google(audio, language='en_gb')
                search = search.lower()
                
                speaker.say(f"searching {search}...")
                webbrowser.get('edge').open_new('https://google.com/search?q=' + search)
                return
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not quite catch that. Please try again")
            speaker.runAndWait()
            
def writing():
    global recognizer
    
    speaker.say("what would you like to write")
    speaker.runAndWait()
    
    done = False

    while done == False:
        try:
            
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
                audio = recognizer.listen(mic)
            
                writing1 = recognizer.recognize_google(audio, language='en_gb')
                writing1 = writing1.lower()
                
                pyautogui.write(f"{writing1}", interval = 0.1)
                return
            
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not quite catch that. Please try again")
            speaker.runAndWait()
        
def hello():
    if name != "":
        speaker.say(f'Welcome back {name}. What can I do for you?')
    else:
        speaker.say('Welcome sir. What can I do for you?')
    print("hi")
    speaker.runAndWait()
    
    
def quit1():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)
    
mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit1,
    "name_writing": write_name,
    "searching": searching_the_web,
    "writing": writing
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

assistant.save_model()

assistant.load_model()

while True:
    
    try:
        with speech_recognition.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            message = recognizer.recognize_google(audio, language='en_gb')
            message = message.lower()
            
        assistant.request(message)
    except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()