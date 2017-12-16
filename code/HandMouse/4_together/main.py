import createMouseXY
import pyb

adc = pyb.ADC('X19')
adc2 = pyb.ADC('X20')
key = pyb.Pin('X1', pyb.Pin.IN)
# hid的1代表按下
hid = pyb.USB_HID()

while True:
	# 归一化
	value_x = adc.read() / 4096
	value_y = adc2.read() / 4096
	# 值匹配
	value_x = value_x * 2 - 1
	value_y = value_y * -2 + 1
	value_left = not key.value()  # 我的这个设备按钮按下是0，所以取反
	# 开始输入
	ret_x, ret_y = createMouseXY.getValue(value_x, value_y)
	# print('value_x:%g,value_y:%g' % (value_x, value_y))
	# print('ret_x:%g,ret_y:%g' % (ret_x, ret_y))
	hid.send((value_left, int(ret_x), int(ret_y), 0))
	pyb.delay(20)
