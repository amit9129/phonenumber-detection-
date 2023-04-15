import pyttsx3

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voices', voices[1].id)
friend . say("Amit , you are my hero"+ "also, I am your subscriber and I like your video")
friend.runAndWait()