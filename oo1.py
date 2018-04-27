class WW:

    def __init__(self):
        self._a = ''
        self.b: int = None

    @property
    def a(self):
        return self._a


class WW1(WW):
    def __init__(self, name: str):
        WW.__init__(self)
        self.name = name


def print_ww(_ww: WW):
    print("a='{}'".format(_ww.a))
    print("b='{}'".format(_ww.b))
    _ww.b = 22
    print("b='{:.6f}'".format(_ww.b))
    _ww.b = 22.55
    print("b='{}'".format(_ww.b))


ww = WW()
print_ww(ww)

ww1 = WW1("peter")
print_ww(ww1)

print("type of ww: {}".format(type(ww)))
print("type of ww1: {}".format(type(ww1)))




