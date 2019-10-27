#import lib_arduino as arduino
import lib_file as file
import lib_transcript as transcript
from playsound import playsound
import random
import time

audio_bonjour_list = ["audio/commentVas_1.mp3","audio/commentVas_2.mp3"]
audio_demande_list = ["audio/demande_1.mp3","audio/demande_2.mp3","audio/demande_3.mp3"]
audio_derien_list = ["audio/derien_1.mp3","audio/derien_2.mp3"]
audio_alarm_list = ["audio/alarm_1.mp3"]
audio_alarmSet_list = ["audio/alarmSet_1.mp3","audio/alarmSet_2.mp3"]
audio_erreur_list = ["audio/erreur_1.mp3"]
audio_merci_list = ["audio/merci_1.mp3","audio/merci_2.mp3"]
audio_ok_list = ["audio/ok_1.mp3","audio/ok_2.mp3","audio/ok_3.mp3","audio/ok_4.mp3","audio/ok_5.mp3"]
audio_pasPossible_list = ["audio/pasPossible_1.mp3","audio/pasPossible_2.mp3"]
audio_repeter_list = ["audio/repeter_1.mp3","audio/repeter_2.mp3"]

audio_focus_list = ["audio/focus_tone.wav"]

def playSound(audio_list):
	audio = random.choice(audio_list)
	try:
		playsound(audio)
		return True
	except:
		return False


while True:
	transcript.veille()
	#Sorti de veille
	playSound(audio_focus_list)
	text = ""
	while "merci" not in text:

		if "bonjour" in text:
			playSound(audio_bonjour_list)

		elif "beau" in text:
			playSound(audio_merci_list)

		text = transcript.listen()

