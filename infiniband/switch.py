class Switch:
    def __init__(self, line):
        self.description = line.strip().split('"')[1]
        line = line.replace('"%s"' % self.description, "")
        parts = line.strip().split()
        self.guid = parts[2]
        self.num_ports = int(parts[4])
        self.port_type = parts[5]
        self.lid = int(parts[9])
        self.lmc = int(parts[11])
        self.ports = {}


    def report(self):
        print self.description
        print "guid         :", self.guid
        print "port type    :", self.port_type
        print "Num of ports :", self.num_ports