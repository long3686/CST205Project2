#this program requires the speech recognition library
#this program requires pyaudio
import os, random, struct, binascii
from Crypto.Cipher import AES
import speech_recognition as sr
def encrytpting(key, input_file, output_file=None, chunksize=64*1024):
    if not output_file:
        output_file = input_file + '.enc'

    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(input_file)

    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
lockedfile = input("What file should be encrypted?" )
key = "fnU229byBYf0XUt81l1QpLTF9vv84Tkc"
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
    print("Your file is encrypted")
    encrytpting(key,lockedfile,lockedfile,16)
else:
    print("You do not have permission to encrypt this file")
