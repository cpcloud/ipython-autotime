from __future__ import print_function

from ._version import version as __version__

from time import strftime, localtime

try:
    from time import monotonic
except ImportError:
    from monotonic import monotonic

from IPython.core.magics.execution import _format_time as format_delta


def format_timestamp(struct_time):
    timestamp = strftime('%Y-%m-%d %H:%M:%S %z', struct_time)
    # add colon in %z (for datetime.fromisoformat, stackoverflow.com/q/44836581)
    return '{}:{}'.format(timestamp[:-2], timestamp[-2:])


class LineWatcher(object):
    """Class that implements a basic timer.

    Notes
    -----
    * Register the `start` and `stop` methods with the IPython events API.
    """
    __slots__ = ['start_time', 'timestamp']

    def start(self):
        self.timestamp = localtime()
        self.start_time = monotonic()

    def stop(self):
        delta = monotonic() - self.start_time
        print(
            u'time: {} (started: {})'.format(
                format_delta(delta),
                format_timestamp(self.timestamp),
            )
        )


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

