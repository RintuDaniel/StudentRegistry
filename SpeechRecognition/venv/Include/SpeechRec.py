#Importing the library
import speech_recognition as sr

#Initialize recognizer
r = sr.Recognizer();

with sr.Microphone() as source:
    print("Speak anything: ")
    #listen to the source
    audio = r.listen(source);
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry could not recognize your voice")
