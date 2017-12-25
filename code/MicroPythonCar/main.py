from pyb import LED, Timer, Pin, Switch, UART, USB_VCP
from Basic.Car_Driver import Car_Driver as Car
from Basic.Wifi_Driver import Wifi_Driver as Wifi
from Basic.ComHelper import ComHelper

sw = Switch()

led1 = LED(1)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)

usb_uart = USB_VCP()

car = Car(['Y1', 'Y2', 'Y3', 'Y4'])
wifi = Wifi()
getter = ComHelper()


def car_control(ret):
    if ret == 'w':
        car.Right_move(1)
        car.Left_move(1)
    elif ret == 's':
        car.Right_move(2)
        car.Left_move(2)
    elif ret == 'a':
        car.Right_move(1)
        car.Left_move(2)
    elif ret == 'd':
        car.Right_move(2)
        car.Left_move(1)
    elif ret == 'x':
        car.Right_move(3)
        car.Left_move(3)


while True:
    led1.toggle()

    getter.add_string(wifi.receive_char())
    getter.add_string(usb_uart.readline())
    ret = getter.get_char()
    if ret is not None:
        print(ret)
        car_control(ret)

    pyb.delay(100)
