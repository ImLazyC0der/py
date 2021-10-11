#pip install pyttsx3

import pyttsx3
friend = pyttsx3.init()
friend.say("Your sentence")
friend.runAndWait()
