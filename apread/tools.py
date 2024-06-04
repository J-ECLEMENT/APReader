import warnings
import functools

def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return new_func

def untilSeconds(chan, seconds):
    """
    Get data from a channel from the start for a certain amount of seconds.
    """
    if chan.isTime:
        return chan.data, chan.data

    if seconds is not None:
        time = chan.Time.data
        data = chan.data
        time = time[time < time[0] + seconds]
        data = data[:len(time)]
        return time, data
    return chan.Time.data, chan.data