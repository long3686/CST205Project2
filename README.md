FileGone
--------

PURPOSE
-------
Senses user via webcam and voice command to enable file encryption to render file unreadable, preventing remote file encryption.

Runs in Python 3.

PERIPHERAL REQUIREMENTS
-----------------------
* Webcam
* Microphone

REQUIRED LIBRARIES
------------------
* pycrypto 2.6.1
* cryptography 1.5.2
* crypto 1.4.1
* OpenCV 3.0
* Speech_Recognition 3.4.6
* NumPy

INSTALLING
----------
* Download Required Libraries
* Download jared.py from github repository here: https://github.com/long3686/CST205Project2

RUNNING
-------
* Run terminal operation python jared.py from local directory
* FileGone will ask for a file to encrypt(text/ image). Specify the filepath.
* FileGone will now look for a face via webcam in order to go to the next step.
* Once a face is recognized, FileGone will ask for a voice password (you can say "password").
* The file will now be encrypted/unreadable.

FUTURE WORK
-----------
* Create a decryption option to restore the file to the original state.
* Create a user specific face recognition with a cascade file.
* Encrypt/ decrypt file folders (batch encryption/ decryption).

MAINTAINERS
-----------
Jared Long - https://github.com/long3686
MooYoung Oh - https://github.com/MOOYOUONGOH
Hugo Hernandez - https://github.com/huhernandez
