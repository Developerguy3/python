import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alice. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def choose_method():
    speak("Hello user how do you want to intarect with me!")
    speak("There are two options")
    engine.say("first ! via voice")
    print("1] via voice")
    engine.say("second ! via keybord")
    print("2] via keybord")
    speak("please select one")
    global choice 
    choice =  int(input())
    print(choice)
   



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
def input_from_keybord():
    inputsrt = input()
    inputsrt = inputsrt.lower()
    return inputsrt

if __name__ == "__main__":
    choose_method()
    
        
    wishMe()
    while True:
        # if 1:
        if(choice==1):
                query = takeCommand().lower()
        elif(choice==2):
                query = input_from_keybord()
                print(query)
        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "dev" in query:
            speak("hello dev")

        elif "open youtube" in query:
            speak("yes sir! opening youtube in your browser")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")   


        elif "play music" in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to harry" in query:
            try:
                speak("What should I say?")
                if(choice==1):
                    content = takeCommand()
                elif(choice==2):
                    content  = input_from_keybord()
                print(query)
                
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email") 
        elif "open camera" in query:
            try:
                speak("yes sir ! opening up ")
                os.startfile("C:\\users\\devsh\\camera")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
        elif "call hiten" in query:
            try:
                speak("yes sir ! calling.... ")
                number = "hiten"
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
        elif "exit" in query:
            try:
                speak("good bye sir ")
                exit()
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
        elif "stop" in query:
            try:
                speak("good bye sir ")
                exit()
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
        elif "alaram" in query:
            try:
                speak("okay")
                exit()
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
