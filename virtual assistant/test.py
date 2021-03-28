import speech_recognition
from datetime import date
from datetime import datetime
import pyttsx3
import webbrowser 
import os


while True:
	robot_ear=speech_recognition.Recognizer()
	with speech_recognition.Microphone()as mic:
		print("Robot: i'm listening ")
		audio=robot_ear.listen(mic)

	print("robot...")
	you= robot_ear.recognize_google(audio)
	print("you :"+you) 

	if "" == you:
		robot_brain=" I can hear you"
	elif "hello" in you :
		robot_brain="hello thu nga "
	elif "today" in you:
		today = date.today()
		robot_brain=today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain= now.strftime("%H:%M:%S")
	elif "youtube"in you:
		robot_brain= webbrowser.open('https://www.youtube.com/',new=1)
	elif "bye" in you:
		robot_brain="bye duy"
		break
	
	print(robot_brain)
	robot_mouth = pyttsx3.init()
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
