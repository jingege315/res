from pyb import Pin


class Car_Driver(object):
    def __init__(self, serve_list):
        assert len(serve_list) == 4
        self.Serve1_1 = Pin(serve_list[0], Pin.OUT_PP)
        self.Serve1_2 = Pin(serve_list[1], Pin.OUT_PP)
        self.Serve2_1 = Pin(serve_list[2], Pin.OUT_PP)
        self.Serve2_2 = Pin(serve_list[3], Pin.OUT_PP)

    # dir=1:向前，=2向后，=3停止
    def Right_move(self, dir=1):
        assert dir == 1 or dir == 2 or dir == 3
        if dir == 1:
            self.Serve1_1.value(0)
            self.Serve1_2.value(1)
        elif dir == 2:
            self.Serve1_1.value(1)
            self.Serve1_2.value(0)
        else:
            self.Serve1_1.value(0)
            self.Serve1_2.value(0)

    # dir=1:向前，=2向后，=3停止
    def Left_move(self, dir=1):
        assert dir == 1 or dir == 2 or dir == 3
        if dir == 1:
            self.Serve2_1.value(1)
            self.Serve2_2.value(0)
        elif dir == 2:
            self.Serve2_1.value(0)
            self.Serve2_2.value(1)
        else:
            self.Serve2_1.value(0)
            self.Serve2_2.value(0)
