import sys
import usb.core
import readline
dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
if dev is None:
    raise ValueError('Device not found')
dev.set_configuration()
while True:  # making a loop
	c = input("$:")
	if "/" == c[0]:
		if c.split("/")[1].split(" ")[0] == "load":
			dev.ctrl_transfer(0x21, 3, 0, 0, "fbclear\n")
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