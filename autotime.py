from __future__ import print_function

import time


class LineWatcher(object):

    """Class that implements a basic timer.

    Notes
    -----
    * Register the `start` and `stop` methods with the IPython events API.
    """

    def __init__(self):
        self.start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        diff = time.time() - self.start_time
        assert diff > 0
        print('time: %s' % format_delta(diff))


def format_delta(num, suffix='s', threshold=1000):
    """Format the result of a timing in different units depending on a
    threshold number of base units.

    Parameters
    ----------
    num : float
    suffix : str
    threshold : int

    Returns
    -------
    fmt : str
        A pretty formatted amount of time

    Notes
    -----
    * Based on http://stackoverflow.com/a/1094933/564538
    """
    base_unit = 1000000000
    num *= base_unit  # smallest unit is 1 / 1000000000 of the biggest unit
    for unit in ['n', 'u', 'm', '']:
        if num < threshold:
            return '%3.2f %s%s' % (num, unit, suffix)
        num /= threshold
    return '%.2f %s' % (num, suffix)


timer = LineWatcher()


def load_ipython_extension(ip):
    ip.events.register('pre_run_cell', timer.start)
    ip.events.register('post_run_cell', timer.stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', timer.start)
    ip.events.unregister('post_run_cell', timer.stop)
