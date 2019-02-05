# Tianxin Zhou 01/25/2019
# For Illumio Coding Assignment

from Firewall import Firewall
fw = Firewall("testcase.csv")

# matches first rule true
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
# matches third rule true
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
# matches second rule true
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))
