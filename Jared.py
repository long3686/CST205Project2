#this program requires the speech recognition library
#this program requires pyaudio
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Voice Recognition Activated, Please State The Passowrd: ")
    audio = r.listen(source)
try:
    print("You stated " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("There was an error recognizing your speech")
except sr.RequestError as e:
    print("There was an error recognizing your speech {0}".format(e))
if r.recognize_google(audio) == 'password':
    print("Your file is unlocked")
else:
    print("Incorrect password")
