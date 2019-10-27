import lib_file as file
import sys

path = "data/user"
file.init(path)#Create file
file.clear(path)#Clear file

file.add(sys.argv[1],path)#Username
file.add(sys.argv[2],path)#Wifi name
file.add(sys.argv[3],path)#Wifi's password