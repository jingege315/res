import pyb

hid = pyb.USB_HID()
key = pyb.Pin('X1', pyb.Pin.IN)
while True:
	hid.send((0, 10, 0, 0))
	pyb.delay(1000)
