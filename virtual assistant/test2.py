import speech_recognition
from datetime import date
import pyttsx3

robot_ear=speech_recognition.Recognizer()
with speech_recognition.Microphone()as mic:
	print("Robot: i'm listening ")
	audio=robot_ear.listen(mic)

you= robot_ear.recognize_google(audio)
print("you :"+you) 


if ""in you:
	robot_brain="Ican hear you"
elif "hello"in you :
	robot_brain="hello duy"
elif "today":
 	
	today = date.today()
	robot_brain = today.strftime("%B %d, %Y")

print(robot_brain)



robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()