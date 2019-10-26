import wikipedia
"""
La librairie wikipedia_lib sert a faciliter les actions de recherches sur wikipedia
"""

wikipedia.set_lang("fr")								#Langue francaise


def search(topic):
	"""
	Effectue un recherche sur le moteur de recherche Wikipedia

	:param str topic: sujet de recherche
	:returns: une liste avec le résultat de la recherche
	"""
	search = wikipedia.search(topic, results=3)			#Effectue la recherche
	return search
	


def content(topic):
	"""
	Recupère le resume des informations concernant le sujet

	:param str topic: sujet de recherche
	:returns: texte contenant les informations resumees
	"""
	content = wikipedia.summary(topic, sentences=2)		#Va chercher les informations
	return content