import pyttsx3


def speak(audio):
       pass      #For now, we will write the conditions later.


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voice[0].id)
def speak(audio):
    
engine.say(audio) 

engine.runAndWait() #Without this command, speech will not be audible to us.