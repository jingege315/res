import pyb

adc = pyb.ADC('X19')
adc2 = pyb.ADC('X20')
key = pyb.Pin('X1', pyb.Pin.IN)
while True:
	print('adc1:%d,adc2:%d,isDown:%d'
		  % (adc.read(), adc2.read(), key.value()))
	pyb.delay(100)
