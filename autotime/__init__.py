from __future__ import print_function

from ._version import version as __version__

try:
    from time import monotonic
except ImportError:
    from monotonic import monotonic

from IPython.core.magics.execution import _format_time as format_delta


class LineWatcher(object):
    """Class that implements a basic timer.

    Notes
    -----
    * Register the `start` and `stop` methods with the IPython events API.
    """
    __slots__ = ['start_time']

    def start(self):
        self.start_time = monotonic()

    def stop(self):
        delta = monotonic() - self.start_time
        print(u'time: {}'.format(format_delta(delta)))


timer = LineWatcher()
start = timer.start
stop = timer.stop


def load_ipython_extension(ip):
    start()
    ip.events.register('pre_run_cell', start)
    ip.events.register('post_run_cell', stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', start)
    ip.events.unregister('post_run_cell', stop)

