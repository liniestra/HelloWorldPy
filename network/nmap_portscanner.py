import nmap

nm = nmap.PortScanner()

nm.scan(hosts="148.204.9.0/24", arguments="-sn")

for host in nm.all_hosts():
    print(host)