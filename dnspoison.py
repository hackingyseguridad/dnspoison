#!/usr/bin/python

from scapy.all import *

def dnsRes(pkt):

    # print pkt[IP].src
    ip = pkt.getlayer(IP)
    dns = pkt.getlayer(DNS)
    return IP(dst=ip.src, src=ip.dst)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=dns.id,qd=dns.qd,an=DNSRR(rrname=dns.qd.qname, type='TXT', ttl=10,rdata='ransom'))
    send(dnsRes(a[0]))
