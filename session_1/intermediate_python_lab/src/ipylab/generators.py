from collections import deque
from statistics import median
from typing import Iterable, Iterator, TypeVar, Deque, Optional

T = TypeVar("T", int, float)

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """
    Yield lists of length `size` from `iterable`. Last chunk may be shorter.
    TODO:
      - Accumulate items into a buffer
      - Yield buffer when size reached; clear and continue
    """
    # TODO: implement
    buffer = []
    for item in iterable:
        buffer.append(item)
        if len(buffer) == size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer
    #return iter(())

def moving_average(window: int):
    """
    Stateful GENERATOR that yields the moving average each time a new value is sent.
    Usage:
        gen = moving_average(5); next(gen)
        out = gen.send(3.0)  # returns current average
    TODO:
      - Keep a deque(maxlen=window)
      - On each .send(x): append x and yield average (sum/len)
    """
    # TODO: implement
    buffer = deque(maxlen=window)
    total = 0.0
    while True:
        value = yield
        if value is None:
            continue
        buffer.append(value)
        avg = sum(buffer) / len(buffer)
        yield avg
    #yield None

def moving_median(window: int):
    """
    Stateful GENERATOR that yields the moving median each time a new value is sent.
    TODO: mirror moving_average but compute statistics.median over the deque.
    """
    # TODO: implement
    buffer = deque(maxlen=window)
    while True:
        value = yield
        if value is None:
            continue
        buffer.append(value)
        med = median(buffer)
        yield med
    #yield None
