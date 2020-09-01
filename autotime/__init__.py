from __future__ import print_function

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


def load_ipython_extension(ip):
    timer.start()
    ip.events.register('pre_run_cell', timer.start)
    ip.events.register('post_run_cell', timer.stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', timer.start)
    ip.events.unregister('post_run_cell', timer.stop)


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
