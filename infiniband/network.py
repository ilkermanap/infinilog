from infiniband.channel_adapter import ChannelAdapter, Port
from infiniband.switch import Switch
from infiniband.node import Node
import infiniband as ib



class Network:
    def __init__(self, name = None, DEBUG = False):
        self.name = name
        self.debug = DEBUG

        self.switches = {}
        self.nodes = {}
        self.discover()

    def report(self):
        for guid,sw in self.switches.items():
            print guid, sw.description

        for name, node in self.nodes.items():
            print name

    def set_name(self, newname):
        self.name = newname

    def discover_nodes(self):
        ndlog, nderr = ib.output("ibhosts", DEBUG=self.debug)
        for line in ndlog:
            x = Node(line)
            self.nodes[x.hostname] = x



    def discover_channel_adapters(self):
        calog, caerr = ib.output("ibqueryerrors", DEBUG=self.debug)
        guid = ""
        hostname = ""
        ca = None
        for line in calog:
            line = line.strip()
            l = line.split()
            l2 = line.split('"')
            if line.find("Data Counters for") > -1:
                guid = l[3]
                hostname = l2[1].split()[0]
                desc = l2[1].split()[1]
                ca = None
                if hostname not in self.nodes.keys():
                    print "%s not found in nodes" % hostname
            if line.find("GUID 0x") > -1:
                portno = int(l[3].replace(":",""))
                print portno
                if ca is None:
                    print "ca create"
                    ca = ChannelAdapter(guid, desc)
                port = Port(number = portno)
                ca.add_port(port)
                values = line.split("[")
                for val in values[1:]:
                    t = val.split()
                    name = t[0]
                    number = int(t[2])
                    ca.ports[portno].set_value(name, number)
                




    def discover_switches(self):
        swlog, swerr = ib.output("ibswitches", DEBUG=self.debug)
        for line in swlog:
            x = Switch(line)
            self.switches[x.guid] = x


    def discover(self):
        self.discover_switches()
        self.discover_nodes()
        self.discover_channel_adapters()


