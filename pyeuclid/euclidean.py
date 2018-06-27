class Euclidean(object):

    def __init__(self, pulses=4, steps=16):
        self._pulses = pulses
        self._steps = steps
        self._pattern = []
        self._remainder = []
        self._counts = []

    def __reset(self):
        self._pattern = []
        self._remainder = []
        self._counts = []

    def __correct(self):
        if self._pulses <= 0:
            raise ValueError
        if self._steps <= 0:
            raise ValueError
        if self._pulses > self._steps:
            temp = self._steps
            self._steps = self.pulses
            self._pulses = temp

    @property
    def pulses(self):
        return self._pulses

    @pulses.setter
    def pulses(self, val):
        self._pulses = val

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, val):
        self._steps = val

    @property
    def rhythm(self):
        return self._pattern

    def __build(self, level):
        if level == -1:
            self._pattern.append(0)
        else:
            if level == -2:
                self._pattern.append(1)
            else:
                for i in range(0, self._counts[level]):
                    self.__build(level - 1)
                if self._remainder[level] != 0:
                    self.__build(level - 2)

    def generate(self):
        self.__correct()
        self.__reset()
        divisor = self.steps - self.pulses
        self._remainder.append(self.pulses)
        level = 0
        while self._remainder[level] > 1:
            self._counts.append(divisor // self._remainder[level])
            self._remainder.append(divisor % self._remainder[level])
            divisor = self._remainder[level]
            level = level + 1

        self._counts.append(divisor)
        self.__build(level)
        pidx = self._pattern.index(1)
        pattern = self._pattern[pidx:] + self._pattern[0:pidx]
        self._pattern = pattern


if __name__ == '__main__':
    EUC1 = Euclidean()
    EUC1.generate()
    print(EUC1.rhythm)
    EUC1.pulses = 4
    EUC1.steps = 17
    EUC1.generate()
    print(EUC1.rhythm)
