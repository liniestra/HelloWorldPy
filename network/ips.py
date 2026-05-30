from scapy.all import ARP, Ether, srp

red = "148.204.9.0/24"

arp = ARP(pdst=red)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

paquete = ether / arp

resultado = srp(paquete, timeout=3, verbose=0)[0]

print("IPs encontradas:")
for enviado, recibido in resultado:
    print(f"IP: {recibido.psrc}  MAC: {recibido.hwsrc}")