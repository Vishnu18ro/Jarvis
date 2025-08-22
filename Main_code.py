import pyttsx3
import speech_recognition as sr
import random
import webbrowser
# import time
import datetime
import os
import pyautogui
from plyer import notification
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib,ssl
from gemini_fn import gemini_intgn
import time

engine=pyttsx3.init()
voic=engine.getProperty('voices')
# //first talk
# variable=pyttsx3.init()
# variable.say("welcome boss")
# variable.runAndWait()

# //voice changer
# engine=pyttsx3.init()
# voic=engine.getProperty('voices')
# for voice in voic:
#     engine.setProperty('voices', voice.id) //no voice[0].id for now coz it is in loop 
#     engine.say("helloooo huhhah boss uh uh uhuh welcome uh uhaahh backkkaa gawkkk gawkk huhhah")
# engine.runAndWait()

# //rate speed
# engine.setProperty('voices',voic[0].id)
# engine.setProperty('rate',200)
# # engine.say("helloooo huhhah boss uh uh uhuh welcome uh uhaahh backkkaa gawkkk gawkk huhhah")
# engine.say("hello boss WELCOME BACK!!")
# engine.runAndWait()


engine.setProperty('voices',voic)
# engine.setProperty('voices',voic[0].id)
engine.setProperty('rate',185)


# //speak fn
def speak(somexyz_parameter):
    engine.say(somexyz_parameter)
    engine.runAndWait()
# speak("hey babes")


# //speech recogn
# r=sr.Recognizer()
# with sr.Microphone() as source:
#     print("say something!" )
#     aud=r.listen(source)
# try:
#     text = r.recognize_google(aud,language='en-in')  # Convert speech to text using Google Web Speech API
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Sorry, I could not understand the audio.")
# except sr.RequestError as e:
#     print(f"Could not request results from Google; {e}")


#speech fn
def speechrec():
    text=" "
    while text==" ":
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("say something!" )
            aud=r.listen(source)
        try:
            text = r.recognize_google(aud,language='en-in')  # Convert speech to text using Google Web Speech API
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
    return text

# //main function
def main_fn():
    while True:
        speechrecgnzed=speechrec().lower()
        if any(keyword in speechrecgnzed for keyword in ["hello","hey","hi"] ) :
            print("hello boss! how can i help u")
            speak("hello boss! how can i help u")
        elif any(keyword in speechrecgnzed for keyword in ["play music","play some music","music","song"]) :
            speak("Playing music")
            song=random.randint(1,5)
            print(f"generated random song number is {song}")
            if song==1:
                print("Playing song Number 1")
                webbrowser.open("https://youtu.be/sPn2HP8cAbo?si=8ar9mI1fe4aUdgZ4")
            elif song==2:
                print("Playing song Number 2")
                webbrowser.open("https://youtu.be/m7gCn9u9bM4?si=eCy3ZwCPcfTZNCLZ")
            elif song==3:
                print("Playing song Number 3")
                webbrowser.open("https://youtu.be/ndLh0CwQx_Y?si=SVso5G9L09X3uOkg")
            elif song==4:
                print("Playing song Number 4")
                webbrowser.open("https://youtu.be/LilMjyEcsfU?si=Amibl4qcYGfDxNdn")
            elif song==5:
                print("Playing song Number 5")
                webbrowser.open("https://youtube.com/shorts/MqIuaLwrgiQ?si=bNe-1-Ajg7VQ9a3_")
        elif "time" in speechrecgnzed:
            now_time=datetime.datetime.now().strftime("%H:%M")
            # speak("Current time is :",str(now_time))// two arg
            speak("Current time is :"+str(now_time))
        elif "date" in speechrecgnzed:
            curr_date=datetime.datetime.now().strftime("%d:%m")
            speak("Today's date is :"+str(curr_date))
        elif "new task" in speechrecgnzed:
            task=speechrecgnzed.replace("new task","").strip()
            if task!="":
                speak("Adding task...."+task)
                print(task)
                with open("todo.txt","a") as file:
                    file.write(task+"\n")
        elif "speak task" in speechrecgnzed:
            with open("todo.txt","r") as file:
                speak("Task to do is: "+file.read())
        elif "show work" in speechrecgnzed: ## can work in mobile also as a notification
            with open("todo.txt","r") as file:
                tasks=(file.read())
            notification.notify(
                title="Today's work: ",
                message=tasks
            )  
        elif "open website" in speechrecgnzed:
            print("which one?")
            speak("which one?")
            webname=speechrec()
            print(f"opening {webname}...")
            speak(f"opening {webname}...")
            webbrowser.open(f"https://{webname}.com")
        elif "open" in speechrecgnzed:
            query=speechrecgnzed.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "screenshot" in speechrecgnzed:
            time_stamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            ss_name=f"screenshot_{time_stamp}.png"
            # ss=speechrecgnzed.replace("screenshot","")
            ss=pyautogui.screenshot()
            ss.save(ss_name) #//save the name as
            print(f"Your screenshot saved as {ss_name}")
            speak("Screenshot taken and saved")
        # ////phase 2 ADVANCED
        elif "wikipedia" in speechrecgnzed:
            # //any var can be used
            speechrecgnzed=speechrecgnzed.replace("jarvis","")
            speechrecgnzed=speechrecgnzed.replace("search wikipedia","")
            result=wikipedia.summary(speechrecgnzed,sentences=2)
            print(result)
            speak(result)
        # //searching in google
        elif any(keyword in speechrecgnzed for keyword in ["search google","search in google","search about","search in google about"]):
            speechrecgnzed=speechrecgnzed.replace("jarvis","")
            speechrecgnzed=speechrecgnzed.replace("search google","")
            speechrecgnzed=speechrecgnzed.replace("search in google","")
            speechrecgnzed=speechrecgnzed.replace("search about","")
            speechrecgnzed=speechrecgnzed.replace("search google about","")
            print(f"Searching about {speechrecgnzed}...")
            speak(f"Searching about {speechrecgnzed}...")
            webbrowser.open(f"https://www.google.com/search?q={speechrecgnzed}")
        # //send whatsapp msg
        elif any(keyword in speechrecgnzed for keyword in ["send whatsapp","send whatsapp message","send message","message now"]):
            speak("sending the message...!!")


            pwk.sendwhatmsg("+91mommy","hi",14,17,30)

        # //METHOD-1 (sending email got resticted for security 2 step verif req)
        elif any(keyword in speechrecgnzed for keyword in ["send email","send mail","send gmail"]):
            speak("GMAIL HAS RESTRICTED ACCESS FOR THIRD PARTY APPS....  NEED TWO STEP VERIFICATION,, CANNOT SEND THE MAIL")
            pwk.send_mail("vishnu18ro@gmail.com",user_config.gmail_password,"subject","msg","recievers_mail@gmail.com")
            speak("email sent")
        # //METHOD-2
        # elif any(keyword in speechrecgnzed for keyword in ["send email","send mail","send gmail"]):
        #     speak("GMAIL HAS RESTRICTED ACCESS FOR THIRD PARTY APPS....  NEED TWO STEP VERIFICATION")
        #     s=smtplib.SMTP('smtp.gmail.com',587)
        #     s.starttls()
        #     s.login("vishnu18ro@gmail.com",user_config.gmail_password)
        #     message="""
        #         this is the message
        #     """
        #     s.sendmail("vishnu18ro@gmail.com",'kodegurukul@gmail.com',message)
        #     s.quit()
        #   speak("email sent")

        elif any(keyword in speechrecgnzed for keyword in ["activate","tibet"]) :
            speechrecgnzed=speechrecgnzed.replace("tibet","")
            print("AI mode activated")
            speak("AI mode activated")
            print("THIS IS BASIC VERSION OF JARVIS.. SO ASK TO THE POINT!!")
            time.sleep(1)
            while True:
                print("Ask Something")
                speechrecgnzed =speechrec()
                if any(keyword in speechrecgnzed for keyword in ["stop","exit"]):
                    print("AI mode exited...")
                    speak("AI mode exited...")
                    break
                reply=gemini_intgn(speechrecgnzed)
                print(reply)
                speak(reply)
        elif any(keyword in speechrecgnzed for keyword in ["stop","exit"]):
            print("Exiting JARVIS..")
            speak("Exiting JARVIS..")
            break
        
# //jarvis features
        
# //song
# //Time
# //date
# //new_task
# //speak_task
# //show_work
# //open_website
# //open_app
# //screenshot
# //wikipedia
# //search_google
# //whatsapp
# //gmail
# //AI


                  


        
main_fn()