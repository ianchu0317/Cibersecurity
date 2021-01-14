import socket
from IPy import IP
import nmap

class Scanner:
    def __init__(self):
        self.hosts = [x for x in range(256)]
        self.scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected_hosts = []
        self.hosts_ports = {}
        self.port_scanner = nmap.PortScanner()

    def check_host_LAN(self, host):
        self.scanner.connect((f"{host}", 135))
        pass


    def port_check(self):
        for host in self.connected_hosts:
            self.port_scanner.scan(f'{host}','')
            pass
        pass


    def main(self):
        for host in self.hosts:
            self.check_host_LAN(host)

        pass