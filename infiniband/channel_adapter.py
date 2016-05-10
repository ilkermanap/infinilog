import time

"""
Ca	: 0xe41d2d03007c1820 ports 2 "klemming-tegner-rtr-2 HCA-1"
Ca	: 0x0002c903004ef76c ports 2 "almqvist-lrtr-1 HCA-1"
Ca	: 0xf45214030087de70 ports 2 "nid00770 HCA-2"
Ca	: 0xf45214030087df30 ports 2 "nid00070 HCA-2"

Data Counters for 0xe41d2d03007c1820 "klemming-tegner-rtr-2 HCA-1"
   GUID 0xe41d2d03007c1820 port 1: [PortXmitData == 19892634015130 (  infPB)] [PortRcvData == 15567487854894 (  infPB)] [PortXmitPkts == 54122042328 (50.405G)] [PortRcvPkts == 54377490509 (50.643G)] [PortUnicastXmitPkts == 54122042287 (50.405G)] [PortUnicastRcvPkts == 54264274186 (50.538G)] [PortMulticastXmitPkts == 52 (52.000)] [PortMulticastRcvPkts == 113216306 (107.971M)]
       Link info:    122   1[  ] ==( 4X          10.0 Gbps Active/  LinkUp)==>  0x0002c90200429160      2   34[  ] "l-2-3 IS5030" ( )
   GUID 0xe41d2d03007c1820 port 2: [PortXmitData == 19182100903731 (  infPB)] [PortRcvData == 14084187130334 (  infPB)] [PortXmitPkts == 40361119808 (37.589G)] [PortRcvPkts == 40651644563 (37.860G)] [PortUnicastXmitPkts == 40361119765 (37.589G)] [PortUnicastRcvPkts == 40538398135 (37.754G)] [PortMulticastXmitPkts == 56 (56.000)] [PortMulticastRcvPkts == 113246412 (108.000M)]
       Link info:    123   2[  ] ==( 4X          10.0 Gbps Active/  LinkUp)==>  0x0002c90200429160      2   23[  ] "l-2-3 IS5030" ( )

"""

class PortStats:
    def __init__(self,line):
        self.date = time.localtime()
        


class Port:
    def __init__(self, number=1 ):
        self.number = number
        self.values = {}
        self.values['speed'] = None

    def set_value(self, name, value):
        self.values[name] = value

    def set_speed(self, new_speed):
        self.values['speed'] = new_speed

    def report(self):
        pass


class ChannelAdapter:
    def __init__(self, guid, desc):
        self.guid = guid
        self.desc = desc
        self.ports = {}

    def add_port(self, port):
        self.ports[port.number] = port
        
    
