import lib_transcript as tr
import lib_file as file
import time

path = "data_cmd_recognization"
file.init(path)
finish = " "
print("Entrainement de la reconnaissance vocale commence dans 3sec")
time.sleep(3)

while(finish not in ['Q','q']):
	text = tr.listen()
	save = input("Voulez vous enregistrer ce texte -" + text + "- (y/n) : ")
	if save=='y':
		file.add(text,path)
		print("Enregistré !")
	else:
		print("Ok on recommence !")
	finish = input("Press q to stop : ")

print(file.read(path))