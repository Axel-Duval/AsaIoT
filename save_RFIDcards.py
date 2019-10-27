import lib_arduino as arduino
import lib_file as file
import re

#Main
file.init("data/uids")
while (len(file.read("data/uids"))<3):
	print("Waiting for a card :")
	res = arduino.get_uid()
	r = re.compile('.*-.*-.*-.*-.*-.*')
	if r.match(res) is not None:
		file.add(res,"data/uids")
	else:
		print("Error")
	print(file.read("data/uids"))