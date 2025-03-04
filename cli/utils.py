import itertools
import sys
import time


def spin_loader(stop_event):
    """
    Displays a spinning loader in the console until the stop_event is set.

    Args:
        stop_event (threading.Event): An event object used to signal the loader to stop.
    """
    spinner = itertools.cycle(["-", "/", "|", "\\"])
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
    sys.stdout.write(" ")
    sys.stdout.flush()
