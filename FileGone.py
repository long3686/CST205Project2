import os, random, struct, binascii
from Crypto.Cipher import AES
import speech_recognition as sr
#project.py must be in the same folder as FileGone.py
import project
import cv2
import numpy as np
#function that does the encrytpting
def encrytpting(key, input_file, output_file=None, chunksize=64*1024):
    #if output_file isn't specified, the encrypted file will be the same as the input_file
    if not output_file:
        output_file = input_file + '.enc'
    #creates a random 16bit iv (initialization vector) for encryption purposes
    iv = os.urandom(16)
    #AES is an encryption algorition programmed in the Cryptography library
    #this particular program uses CBC mode or cipher block chaining
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(input_file)
    #opens the file to be encrypted
    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            #writes the randomly generated initialization vector to the outfile
            outfile.write(iv)
            #reads the chosen file chunk by chunk, and adds spaces if necessary
            while True:
                chunk = infile.read(chunksize)
                #if no more chunks are left, end the loop
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                #writes the encrypted chunk to the new file
                outfile.write(encryptor.encrypt(chunk))
#prompts the user to input a file to be encrypted, input the full file path
lockedfile = input("What file should be encrypted?" )
#randomly generated 16 bit key to use in encryption, feel free to use your own
key = "fkU239bvBYf1XUt91g1QpLTF0vw84Pkj"
speechRecog = sr.Recognizer()
#if a face is found, then speech recognition is turned on
if x in faces > 0 and y in faces > 0 and w in faces > 0 and h in faces > 0:
    #uses the microphone as a source for speech recognition, sensitivity will vary, best done in a quiet room
    with sr.Microphone() as source:
        print("Voice Recognition Activated, Please State The Passowrd: ")
        audio = speechRecog.listen(source)
    try:
        print("You stated " + speechRecog.recognize_google(audio))
        #Uses the google API for recognizing speech, this program requires internet connection
    except sr.UnknownValueError:
        print("There was an error recognizing your speech")
    except sr.RequestError as e:
        print("There was an error recognizing your speech {0}".format(e))
    #if the recognizer hears you say "password"
    if speechRecog.recognize_google(audio) == 'password':
        print("Your file is encrypted")
        #runs the encrytption function
        encrytpting(key,lockedfile,lockedfile,16)
    else:
        print("You do not have permission to encrypt this file")
#if no face is detected, do not prompt for speech or allow encryption
else:
    print ("No faces detected by the camera, permission not granted")
