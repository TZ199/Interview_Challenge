# Tianxin Zhou 01/25/2019
# For Illumio Coding Assignment
# Python version 3.6.5
import csv


class Firewall(object):
    csvfile = ""
    map = {}

    def __init__(self, csvfile):
        # Initial the rules of Firewall
        self.map["inbound"] = {}
        self.map["outbound"] = {}
        self.map["inbound"]["tcp"] = {}
        self.map["inbound"]["udp"] = {}
        self.map["outbound"]["tcp"] = {}
        self.map["outbound"]["udp"] = {}
        # Read in CSV file
        self.csvfile = csvfile
        f = open(csvfile, 'r')
        reader = csv.reader(f)
        # Read rules into Map
        for row in reader:
            # Get the variables from csv file line by line
            direction, protocol, port, ip = row
            ports = self.map[direction][protocol]
            if port in ports:
                self.map[direction][protocol][port].append(ip)
            else:
                self.map[direction][protocol][port] = [ip]

    # Fucntion to determine if the packet is valid
    # Variables: idirection, iprotocol, iport, iip
    # Output : T or F
    def accept_packet(self, idirection, iprotocol, iport, iip):
        portmap = self.map.get(idirection).get(iprotocol)
        if not portmap:
            return False
        # Traverse for every port and their ips
        for ports, ips in portmap.items():
            if self.checkport(ports, iport):
                for ip in ips:
                    if self.checkip(ip, iip):
                        return True
        return False

    # Help function to check port number
    def checkport(self, ports, iport):
        index = ports.find("-")
        iport = int(iport)
        if index >= 0:
            lowerbound = int(ports[:index])
            upperbound = int(ports[index + 1:])
            if iport <= upperbound and iport >= lowerbound:
                return True
        else:
            if iport == int(ports):
                return True
        return False

    # Help function to check ip number
    def checkip(self, ips, iip):
        iip = int(iip.replace(".", ""))
        index = ips.find("-")
        if index >= 0:
            lowerbound = int(ips[:index].replace(".", ""))
            upperbound = int(ips[index + 1:].replace(".", ""))
            if iip <= upperbound and iip >= lowerbound:
                return True
        else:
            if iip == int(ips.replace(".", "")):
                return True
        return False
