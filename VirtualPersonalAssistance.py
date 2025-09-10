import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
from plyer import notification
import pyautogui
import pywhatkit as pwk
from mtranslate import translate
import user_pass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis Mam , please tell me how can i help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("tidakeshruti19@gmail.com", user_pass.gmail_password)  # FIXED
        server.sendmail("tidakeshruti19@gmail.com", to, content)
        server.close()
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search google' in query:
            query = query.replace("jarvis", "")
            query = query.replace("search google", "").strip()
            speak(f"Searching Google for {query}")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            speak("Playing music")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=NOJkx7QcBHk")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=6SEIBCSnGQM")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=l8asg-CPF5E")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\shrut\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'new task' in query:
            task = query.replace("new task", "").strip()
            if task != "":
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif 'read task list' in query:
            try:
                with open("todo.txt","r") as file:   # FIXED typo
                    speak("Work we have to do today is: "  + file.read())
            except FileNotFoundError:
                speak("No tasks found.")

        elif 'give me a notification of task' in query:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                    if tasks:
                        notification.notify(
                            title="Today's Work",
                            message=tasks,
                            timeout=10
                        )
                        speak("Here are your tasks for today.")
                    else:
                        speak("Your to-do list is empty.")
                        notification.notify(
                            title="Today's Work",
                            message="No tasks found.",
                            timeout=10
                        )
            except FileNotFoundError:
                speak("I could not find your to-do list file.")

        elif 'open' in query:
            request = query.replace('open',"").strip()
            pyautogui.press("super")
            pyautogui.typewrite(request)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'send whatsapp' in query:
            speak("Sending WhatsApp message.")
            pwk.sendwhatmsg("+919975638745", "Hi, how are you", 22, 58, 15)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver@gmail.com"
                if sendEmail(to, content):
                    speak("Email has been sent successfully!")
                else:
                    speak("Sorry, I was not able to send the email.")
            except Exception as e:
                speak("Some error occurred. Please try again.")
                
               