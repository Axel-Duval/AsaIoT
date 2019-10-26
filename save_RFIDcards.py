import lib_arduino as arduino
import lib_file as file
import re

#Main
file.init("data_uid")
while (len(file.read())<3):
	print("Waiting for a card :")
	res = arduino.get_uid()
	r = re.compile('.*-.*-.*-.*-.*-.*')
	if r.match(res) is not None:
		file.add(res)
	else:
		return TypeError
	print(file.read())