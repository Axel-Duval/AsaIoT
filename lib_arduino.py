# Import de la librairie serial
import serial

# Ouverture du port serie avec :
# 115200 : vitesse de communication
serialArduino = serial.Serial('/dev/ttyACM0', 115200)

def get_uid():
	# Recuperation de l'uid
  	uid = serialArduino.readline().decode("UTF-8")[:-2]
  	return uid
