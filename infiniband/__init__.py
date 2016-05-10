from infiniband.channel_adapter import ChannelAdapter
from infiniband.switch import Switch
from infiniband.network import Network
from infiniband.switchport import SwitchPort

from subprocess import Popen, PIPE


def output(cmd, args = None, DEBUG = False):
    if DEBUG is False:
        if args is None:
            newargs = [cmd]
        else:
            newargs = [cmd] + args
        proc = Popen(newargs, stdout = PIPE, stderr=PIPE)
        log, err = proc.communicate()
        return (log, err)
    else:
        if args is None:
            return (open("sample/%s.txt" % cmd, "r").readlines(),[])
        else:
            pass