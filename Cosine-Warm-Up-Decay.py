"""
@Author: zhkun
@Time:  16:24
@File: Cosine-Warm-Up-Decay
@Description:
@Something to attention
"""
import math


class CosineDecay(object):

    def __init__(self,
                 max_value,
                 min_value,
                 num_loops):
        self._max_value = max_value
        self._min_value = min_value
        self._num_loops = num_loops

    def get_value(self, i):
        if i < 0:
            i = 0
        if i >= self._num_loops:
            i = self._num_loops - 1
        value = (math.cos(i * math.pi / self._num_loops) + 1.0) * 0.5
        value = value * (self._max_value - self._min_value) + self._min_value
        return value


class CosineWarmUp(object):

    def __init__(self,
                 max_value,
                 min_value,
                 num_loops):
        self._max_value = max_value
        self._min_value = min_value
        self._num_loops = num_loops

    def get_value(self, i):
        if i < 0:
            i = 0
        if i >= self._num_loops:
            i = self._num_loops - 1
        i = i - self._num_loops + 1
        value = (math.cos(i * math.pi / self._num_loops) + 1.0) * 0.5
        value = value * (self._max_value - self._min_value) + self._min_value
        return value


class CosineWarmUpDecay(object):

    def __init__(self,
                 max_value,
                 min_value,
                 num_loops,
                 warm_up=0.05):
        self._max_value = max_value
        self._min_value = min_value
        self._num_loops = num_loops
        self._warm_up_p = warm_up
        self._warm_up = CosineWarmUp(max_value, min_value, int(num_loops * warm_up))
        self._decay = CosineDecay(max_value, min_value, int(num_loops * (1.0 - warm_up)))

    def get_value(self, i):
        if i < self._num_loops * self._warm_up_p:
            return self._warm_up.get_value(i)
        else:
            return self._decay.get_value(i)


class ExponentialDecay(object):

    def __init__(self,
                 init_value,
                 min_value,
                 num_loops):
        self._init_value = init_value
        self._min_value = min_value
        self._num_loops = num_loops

        self._value = init_value
        self._step = math.pow(min_value / init_value, 1.0 / num_loops)

    @property
    def value(self):
        return self._value

    def next(self):
        if self._value > self._min_value:
            self._value = self._value * self._step
            if self._value < self._min_value:
                self._value = self._min_value
        return self._value

    def reset(self):
        self._value = self._init_value
