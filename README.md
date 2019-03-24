# dnspoison



from scapy.all import *

answer = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.thepacketgeek.com")),verbose=0)
print answer[DNS].summary()

Respuesta DNS Scapy:
               spfResp = IP (dst = pkt [IP] .src, src = pkt [IP] .dst) \ 
                    /UDP(dport=pkt[UDP◆.sport, sport = 53) \ 
                    / DNS (id = pkt [DNS]). id, \ 
                              qr = 1L, \ 
                              qd = DNSQR (qname = pkt [DNSQR] .qname), \ 
                              an = DNSRR (rrname = "trailers.apple.com", rdata = localIP) \ 
                              )
