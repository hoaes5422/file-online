from datetime import date
import pyttsx3
import speech_recognition
robot_mouth  = pyttsx3.init()
robot_mouth.say("what do you need,sir please enter below,if you want to write,choose write")
robot_mouth.runAndWait()
robot_mouth  = pyttsx3.init()
robot_mouth.say("and if you choose speak please write speak")
robot_mouth.runAndWait()


ha = input()
if ha == "write":
	print("So you choose write Sir, please enter what you need,I'm AI,please to meet you")
	while True:
		ban = input()	
		if "hello" in ban:
			robot_brain = "Hello sir"
		elif "today" in ban:
			today = date.today()
			robot_brain	= "today is" + 	today.strftime("%B %d, %Y")
			print(today.strftime("%B %d, %Y"))
		elif "bye" in ban:
			robot_brain = "Goodbye sir, have a good day"
			robot_mouth  = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()
			break	
		else: 
			robot_brain = "I can't understand what you write sir,please enter again"

		robot_mouth  = pyttsx3.init()
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
elif ha == "speak":
	print("so you choose speak sir ,please to meet you, my name is AI,please speak what you need")
	while True:
		robot_ear = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
				print("I'm listening")
				audio = robot_ear.listen(mic)
		try:
			ban = robot_ear.recognize_google(audio)
		except:
			ban = ""
		if "hello" in ban:
			robot_brain = "Hello richard"
			robot_mouth  = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()
		elif "today" in ban:
			today = date.today()
			robot_brain	= today.strftime("%B %d, %Y")
			print(today.strftime("%B %d, %Y"))
			robot_mouth  = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()
		elif "bye" in ban:
			robot_brain = "Goodbye sir, have a good day"
			robot_mouth  = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()
			break	
		else: 
			robot_brain = "I can't understand what you say sir,please say again"
			robot_mouth  = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()
else:
	robot_mouth  = pyttsx3.init()
	robot_mouth.say("please enter again")
	robot_mouth.runAndWait()















