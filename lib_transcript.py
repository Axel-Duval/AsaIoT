import speech_recognition as sr
"""
La librairie transcript_lib sert a convertir un format audion en texte
"""
r = sr.Recognizer()

def listen():
	"""
	Fonction qui ecoute et transcrit l'audio
	
	:returns: le texte transcrit sinon une erreur
	"""
	with sr.Microphone() as source:								#Definition du micro comme source
		print("Speak : ")
		r.adjust_for_ambient_noise(source)
		r.pause_threshold = 0.3
		r.non_speaking_duration = 0.2							#Ajustement de l'environnement
		audio = r.listen(source)								#Ecoute la source

		try:
			text = r.recognize_google(audio,language='fr-FR')	#Transcription de l'audio
			return text
		except:
			print("Désolé je n'ai pas compris veuillez recommencer")
			listen()
		return ValueError