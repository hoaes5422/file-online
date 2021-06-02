import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
		print("I'm listening")
		audio = robot_ear.listen(mic)
try:
	ban = robot_ear.recognize_google(audio)
except:
	ban = ""