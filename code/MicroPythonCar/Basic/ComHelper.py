class ComHelper(object):
    def __init__(self, newline='\r'):
        self.newline = newline
        self.recstr = ''

    def add_string(self, str_add):
        if str_add is not None:
            if isinstance(str_add, bytes):
                str_add = str_add.decode('utf-8')
            self.recstr += str_add

    def get_line(self):
        if self.newline in self.recstr:
            index = self.recstr.index(self.newline)
            ret = self.recstr[:index]
            recstr2 = self.recstr[index + 1:]
            self.recstr = recstr2
            return ret
        return None

    def get_Int(self):
        temp = self.get_line()
        try:
            temp = int(temp)
        except Exception:
            pass
        else:
            return temp
        return None

    def get_char(self):
        if len(self.recstr) == 0:
            return None
        ret = self.recstr[0]
        self.recstr = self.recstr[1:]
        return ret
