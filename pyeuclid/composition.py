class Composition(object):
    def __init__(self):
        self._ppqn = 24
        self._beat = 4
        self._bar = 4

    @property
    def ppqn(self):
        return self._ppqn

    @ppqn.setter
    def ppqn(self, val):
        self._ppqn = val

    @property
    def beat(self):
        return self._beat

    @beat.setter
    def beat(self, val):
        self._beat = val

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, val):
        self._bar = val
        
