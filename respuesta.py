                spfResp = IP(dst=pkt[IP].src, src=pkt[IP].dst)\
                    /UDP(dport=pkt[UDP].sport, sport=53)\
                    /DNS(id=pkt[DNS].id, \
                              qr=1L,\
                              qd=DNSQR(qname=pkt[DNSQR].qname), \
                              an=DNSRR(rrname=”trailers.apple.com”,rdata=localIP) \
                              )
