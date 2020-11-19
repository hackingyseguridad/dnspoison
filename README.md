# dnspoison


Envio de respuestas falsas de dns con id 65535, para envenamiento:


#python3 dnspoison.py


Para que se produzca el evenenamiento, es necesario inundar de respuestas DNS y hacer coincidir el ID y el numero puerto UDP de respuesta. 

Para averiguar al puerto de respuesta utilizaremos la respuesta ICMP. ICMPtest.sh


<img style="float:left" alt="dns poisoning logo" src="https://github.com/hackingyseguridad/dnspoison/blob/master/envenamiento.png">

Referencias:

https://en.wikipedia.org/wiki/DNS_spoofing#Cache_poisoning_attacks

https://github.com/bluecatlabs/network-vip/tree/main/icmp_ratelimit

#
# www.hackingyseguridad.com 
#
                             
