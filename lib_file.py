import os
import pickle

"""
La librairie file_lib sert a faciliter les actions avec tout type de fichier
"""


def init(path):
	"""
	Initialisation du fichier s'il n'est pas deja cree

	:param str path: chemin et nom du fichier
	:returns: True si il a ete initialise sinon False
	"""
	try:
 		with open(path): pass						#On teste si le fichier est deja cree s'il il l'est on ne fait rien
	except IOError:									#Le fichier n'est pas cree
		init = []									#Initialisation du tableau 
		with open(path,'wb') as file:
				pickle.Pickler(file).dump(init)		#Enregistrement du tableau
				return True
	return False

def read(path):
	"""
	Lecture du fichier pour recuperer son contenu

	:param str path: chemin et nom du fichier
	:returns: Le tableau contenant des donnees
	"""
	with open(path,'rb') as file:
		return pickle.Unpickler(file).load()

def add(data,path):
	"""
	Ajout d'un element dans le fichier

	:param str data: l'element a ajouter
	:param str path: chemin et nom du fichier
	:returns: True si l'element a ete ajoute sinon False
	"""
	liste_uid = read(path)							#Recuperation de la liste
	if (not data in liste_uid):						#On verifie qu'il n'existe pas deja
		liste_uid.append(data)						#Ajout de l'uid dans la liste
		save(liste_uid,path)						#Enregistrement du tableau
		return True
	else:
		return False

def remove(data,path):
	"""
	Suppression d'un element dans le fichier

	:param str data: l'element a supprimer
	:param str path: chemin et nom du fichier
	:returns: True si l'element a ete supprime sinon False
	"""
	liste_uid = read(path)							#Recuperation de la liste
	if(data in liste_uid):							#Verification que l'element est dans le fichier
		liste_uid.remove(data)						#Supression de l'element
		save(liste_uid,path)						#Enregistrement du tableau
		return True
	else:
		return False

def count(path):
	"""
	Compte le nombre d'element dans le fichier

	:param str path: chemin et nom du fichier
	:returns: le nombre d'elements du fichier
	"""
	return len(read(path))

def save(data,path):
	"""
	Enregistrement de la donnee dans le fichier
	
	:param None data: la donnee a enregistrer
	:param str path: chemin et nom du fichier
	:returns: True si la sauvegarde a ete faite sinon False
	"""
	with open(path,'wb') as file:
			pickle.Pickler(file).dump(data)			#Enregistrement du tableau
			return True
	return False