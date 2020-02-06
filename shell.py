import sys
import usb.core
import readline
if sys.version[0] != 3:
	print("although this script works in Python 2 it will be unsupported for this script and will only use Python 3")
dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
if dev is None:
    raise ValueError('Device not found')
dev.set_configuration()
while True:  # making a loop
	if sys.version[0] == 3:
		c = input("$:")
	elif sys.version[0] == 2:
		c = raw_input("$:")
	if "/" == c[0]:
		if c.split("/")[1].split(" ")[0] == "load":
			data = open(c.split(" ")[1], "rb").read()
			dev.ctrl_transfer(0x21, 2, 0, 0, 0)
			dev.ctrl_transfer(0x21, 1, 0, 0, 0)
			dev.write(2,data,100000)
			if len(data) % 512 == 0:
				dev.write(2,"")
			dev.ctrl_transfer(0x21, 3, 0, 0, "modload\n")
		if c.split("/")[1].split(" ")[0] == "loadb":
			data = open(c.split(" ")[1], "rb").read()
			dev.ctrl_transfer(0x21, 2, 0, 0, 0)
			dev.ctrl_transfer(0x21, 1, 0, 0, 0)
			dev.write(2,data,100000)
			if len(data) % 512 == 0:
				dev.write(2,"")
			dev.ctrl_transfer(0x21, 3, 0, 0, "modload\n")
			dev.ctrl_transfer(0x21, 3, 0, 0, "bootx\n")
	else:
		dev.ctrl_transfer(0x21, 3, 0, 0, c + "\n")	
