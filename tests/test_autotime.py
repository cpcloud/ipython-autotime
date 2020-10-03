from IPython import get_ipython
from IPython.testing import tools as tt
from IPython.terminal.interactiveshell import TerminalInteractiveShell


def test_full_cycle():
    shell = TerminalInteractiveShell.instance()
    ip = get_ipython()

    with tt.AssertPrints('time: '):
        ip.run_cell('%load_ext autotime')

    with tt.AssertPrints('time: '):
        ip.run_cell('x = 1')

    with tt.AssertNotPrints('time: '):
        ip.run_cell('%unload_ext autotime')
