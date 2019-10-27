import speech_recognition as sr
"""
La librairie transcript_lib sert a convertir un format audion en texte
"""
r = sr.Recognizer()

def listen():
	"""
	Fonction qui ecoute et transcrit l'audio
	
	:returns: le texte transcrit sinon False
	"""
	with sr.Microphone() as source:						#Definition du micro comme source
		r.operation_timeout = 3
		r.adjust_for_ambient_noise(source)
		r.pause_threshold = 0.3
		r.non_speaking_duration = 0.3					#Ajustement de l'environnement
		audio = r.listen(source)						#Ecoute la source
	try:
		text = r.recognize_google(audio,language='fr-FR')	#Transcription de l'audio
		print(text)
		return text.lower()
	except:
		return ""


def veille():
	text = ""
	while "alexa" not in text:
		text = listen()
	print("sorti de veille")

