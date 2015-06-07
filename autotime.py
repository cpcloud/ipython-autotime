from __future__ import print_function

import time


class LineWatcher(object):
    def __init__(self, ip):
        self.shell = ip
        self.start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        print('time: %.6f s' % (time.time() - self.start_time))


def load_ipython_extension(ip):
    timer = LineWatcher(ip)
    ip.events.register('pre_run_cell', timer.start)
    ip.events.register('post_run_cell', timer.stop)


def unload_ipython_extension(ip):
    timer = LineWatcher(ip)
    ip.events.unregister('pre_run_cell', timer.start)
    ip.events.unregister('post_run_cell', timer.stop)
