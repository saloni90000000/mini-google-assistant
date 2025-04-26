import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import webbrowser
import pywhatkit as kit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
     engine.say(audio)
     print(audio)
     engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said:{query}")
    except Exception as e:
        speak("say that again")
        return "none"
    return query

def greet( ):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning ")
        speak(" Hey I am jarvis . How can I help you?")

    elif hour>12 and hour<18:
        speak("good afternoon")
        speak(" Hey i am jarvis . How can i help you?")

    else:
        speak("good evening")
        speak(" Hey i am jarvis . How can i help you?")



if _name=="main_":
   #speak("hii ")
   # takecommand()
   greet()
   if 1:
       query = takecommand().lower()
       if "open camera" in query:
          cap = cv2.VideoCapture(0)
          while True:
              ret, img = cap.read()
              cv2.imshow('webcam',img)
              k = cv2.waitKey(50)
              if k==27:
                  break;
          cap.release()
          cv2.destroyAllWindows()

       elif "open notepad" in query:
          path = "C:\\Windows\\system32\\notepad.exe"
          os.startfile(path)

       elif "open command prompt" in query:
          os.system("start")

       elif "ip address" in query:
          ip = get('https://api.ipify.org').text
          speak(f"your IP address is {ip}")

       elif "open youtube" in query:
           webbrowser.open("www.youtube.com")

       elif "open wikipedia" in query:
           webbrowser.open("www.wikipedia.com")

       elif "open google" in query:
           speak("what should I search?")
           cm = takecommand().lower()
           webbrowser.open(f"{cm}")

       elif "send message" in query:
           kit.sendwhatmsg("+918958657742","hello",2,25 )

       elif "play songs on youtube" in query:
           kit.playonyt("hass hass")

       elif "no thanks" in query:
           speak("thanks for using me,have a nice day")
           sys.exit()

       speak("thanks for using me,have a nice day")
       sys.exit()
