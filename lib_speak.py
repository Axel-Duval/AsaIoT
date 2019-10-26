from gtts import gTTS
"""
La librairie speak_lib sert a convertir un texte en format audio
"""

def speak(text,path):
	"""
	Fonction qui enregistre un fichier au format .mp3 avec l'audio de la phrase
	
	:param str text: la phrase a lire
	:returns: True et un fichier .mp3 avec l'audio de la phrase sinon False
	"""
	try:
		output = gTTS(myText,'fr',False)			#Creation de l'audio
		output.save(path)							#Sauvegarde du fichier .mp3
		return True
	return False
