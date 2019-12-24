from concurrent.futures import ThreadPoolExecutor, as_completed

import pytest

from yahoofinance.query.QueryUtils import *


def seconds_to_nanoseconds(sec):
    return sec * 1000000000


@pytest.mark.parametrize("init_count", [-1, -5, -10000, -317])
def test_countdown_no_negative(init_count):
    with pytest.raises(ValueError):
        countdown = Countdown(init_count)


@pytest.mark.parametrize("init_count", [3.14, "3.14", [3], {3}])
def test_countdown_requires_int(init_count):
    with pytest.raises(ValueError):
        countdown = Countdown(init_count)


@pytest.mark.parametrize("init_count", [1, 10, 100, 1000])
def test_countdown_initialization(init_count):
    countdown = Countdown(init_count)
    assert (not countdown.finished())


@pytest.mark.parametrize("init_count", [1, 10, 100, 1000])
def test_countdown_decrement(init_count):
    countdown = Countdown(init_count)
    for i in range(init_count):
        res = countdown.dec_count()
        assert res

    assert (countdown.finished())


@pytest.mark.parametrize("init_count", [1, 10, 100, 1000])
def test_countdown_decrement_threaded(init_count):
    countdown = Countdown(init_count)
    futures = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        for i in range(init_count):
            futures.append(executor.submit(lambda c: c.dec_count(), countdown))

        for f in as_completed(futures):
            assert (f.result())

    assert (countdown.finished())


@pytest.mark.parametrize("init_count", [-1, -100000, -3.14, -22343325.4])
def test_countdown_time_no_negative(init_count):
    with pytest.raises(ValueError):
        countdown = CountdownTime(init_count)


@pytest.mark.parametrize("init_count", ["3.2445", [1.3525], {3}])
def test_countdown_time_requires_int_or_float(init_count):
    with pytest.raises(ValueError):
        countdown = CountdownTime(init_count)


@pytest.mark.parametrize("seconds", [3.2445, 1.3525, 3])
def test_countdown_time_initialization(seconds):
    nanoseconds = seconds_to_nanoseconds(seconds)
    countdown = CountdownTime(nanoseconds)
    assert (countdown.time_left() >= 0)


@pytest.mark.parametrize("seconds", [3.2445, 1.3525, 3])
def test_countdown_time_sec_initialization(seconds):
    nanoseconds = seconds_to_nanoseconds(seconds)
    countdown = CountdownTime(nanoseconds)
    assert (countdown.time_left_sec() >= 0)


@pytest.mark.parametrize("seconds", [3, 5.5, 11.17, 32])
@pytest.mark.parametrize("ratio", [1, 1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0, 10.0, 100.0, 1000.0])
def test_countdown_time_time_left(seconds, ratio):
    nanoseconds = seconds_to_nanoseconds(seconds)
    frac_sec = seconds / ratio
    countdown = CountdownTime(nanoseconds)
    time.sleep(frac_sec)
    assert (countdown.time_left() <= seconds_to_nanoseconds(seconds - frac_sec))


@pytest.mark.parametrize("seconds", [3, 5.5, 11.17, 32])
@pytest.mark.parametrize("ratio", [1, 1.1, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0, 8.0, 10.0, 100.0, 1000.0])
def test_countdown_time_time_left_sec(seconds, ratio):
    nanoseconds = seconds_to_nanoseconds(seconds)
    frac_sec = seconds / ratio
    countdown = CountdownTime(nanoseconds)
    time.sleep(frac_sec)
    assert (countdown.time_left_sec() <= seconds - frac_sec)
