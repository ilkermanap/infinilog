from infiniband.channel_adapter import ChannelAdapter

class Node:
    def __init__(self, line):
        self.hostname = line.split('"')[1].split()[0]
        self.adapters = {}

    def add_adapter(self, adapter):
        self.adapters[apadter.guid] = adapter