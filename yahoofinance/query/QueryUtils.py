import time
from threading import Lock


class Countdown:
    """
    Starts with an initial number, and allows that number to be decremented in thread-safe manner.
    """

    def __init__(self, init_count: int):
        """
        :param init_count: The initial number to count down from. Throws value error if less than zero.
        """
        if not isinstance(init_count, int):
            raise ValueError("Initial Count should be an integer!")
        if init_count < 0:
            raise ValueError("JobCount should not be negative")
        self.__count__ = [init_count]
        self.__lock__ = Lock()

    def dec_count(self, blocking=True, timeout=-1):
        """

        :param blocking: Whether we should block when trying to decrement the current count. Defaults to true.
        :param timeout:  How much time should be spend waiting to decrement the current count. By default, program will
            wait indefinitely.
        :return: Whether we were successfully able to decrement the count.
        """
        if not self.finished():
            res = self.__lock__.acquire(blocking=blocking, timeout=timeout)
            if res:
                if self.__count__[0] > 0:
                    self.__count__[0] -= 1
                self.__lock__.release()
            return res
        return True

    def finished(self) -> bool:
        """
        :return: True if countdown if finished, false otherwise.
        """
        return self.__count__[0] == 0


class CountdownTime:
    """
    Starts with an initial count of time (in nanoseconds), and automatically keeps track
    of how much of that time is left.
    """

    def __init__(self, init_ns):
        """
        :param init_ns: The initial amount of time (in nanoseconds) to count down from.
        """
        if not isinstance(init_ns, float) and not isinstance(init_ns, int):
            raise ValueError("Initial nanoseconds must be int or float!")
        if init_ns < 0:
            raise ValueError("Initial nanoseconds should not be negative!")
        self.ns = init_ns

    def time_left(self) -> float:
        """

        :return:  The amount of time left in our countdown (in nanoseconds).
        """
        curr = time.monotonic_ns()
        if curr > self.ns:
            return 0
        else:
            self.ns -= curr
            return self.ns

    def time_left_sec(self) -> float:
        """

        :return: The amount of time left in our countdown (in seconds).
        """
        return self.time_left() / 1000000000.0
