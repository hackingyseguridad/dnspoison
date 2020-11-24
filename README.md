# dnspoison


Envio de respuestas falsas de dns con id 65535, para envenamiento:


#python3 dnspoison.py


Para que se produzca el evenenamiento, es necesario inundar de respuestas DNS modificadas y hacer coincidir el ID de respuesta y el numero puerto UDP. 




<img style="float:left" alt="dns poisoning logo" src="https://github.com/hackingyseguridad/dnspoison/blob/master/envenamiento.png">


La vulnerabilidad de envenenamiento se debía a una implementación débil del sistema generador de números pseudo-aleatorios que se utilizan como  ID identificador único de cada petición DNS. La debi-lidad de este sistema está ocasionada por el uso del identificador del proceso (PID) y la hora actual como "semilla" para generar los números aleatorios ID.

Este ID sirve como identificador único en los paquetes que conforman la petición y luego la respuesta.

Si el identificador generado para cada consulta no es suficientemente aleatorio y llega a ser predicho de alguna manera, el atacante solo tiene que inundar al resolver de paquetes UDP con una pequeña can-tidad de respuestas DNS. La que coincida será tomada como buena por el dispositivo que intenta resol-ver, haciendo que redirija los paquetes del atacante en vez de al servidor DNS legítimo consultado.
Si por el contrario el sistema de resolución realmente elige números aleatorios, las posibilidades del atacante son mínimas y necesitaría años para poder engañar al dispositivo.

Referencias:

https://en.wikipedia.org/wiki/DNS_spoofing#Cache_poisoning_attacks

https://github.com/bluecatlabs/network-vip/tree/main/icmp_ratelimit

#
# www.hackingyseguridad.com 
#
                             
