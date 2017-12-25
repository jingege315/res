from pyb import UART


# 处理单字节的内容，字节已字符串表示
class Wifi_Driver(object):
    def __init__(self, uart_num=2, uart_baud=9600):
        self.uart = UART(uart_num, uart_baud)
        self.uart.init(uart_baud, bits=8, parity=None, stop=1)

    def receive_char(self):
        temp = self.uart.readchar()
        if temp == -1:
            return None

        temp = chr(temp)
        return temp
