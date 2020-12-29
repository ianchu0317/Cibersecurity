import socket
from IPy import IP


def check_ip(ip):
    try:
        return IP(ip)
    except ValueError:
        return socket.gethostbyname(str(ip))


def scan_port(addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    check_ip(addr)
    #print(f"{addr} Information: ")
    try:
        sock.settimeout(0.5)
        sock.connect((addr, port))
        print(f"[+] Port {port} is open")
        print(get_info(sock))
    except:
        #print(f"[-] Port {port} is closed")
        pass


def scan_targets(target):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"{target} Information: ")
    for port in range(79, 86+1):
        try:
            sock.settimeout(0.5)
            sock.connect((target, port))
            print(f"[+] Port {port} is open")
        except:
            pass


def get_info(sock):
    return sock.rcv(1024)

ip_addr = input ("[+] Enter a ip address to scan: ")

if "," in ip_addr:
    ip = ip_addr.split(",")
    for target in ip:
        target = target.strip(" ")
        check_ip(str(target))
        print(f"{target} Information: ")
        for port in range(79, 85):
            scan_port(target, port)

#    This is the other option to use
#    scan_targets(target)

else:
    check_ip(ip_addr)
    print(f"{ip_addr} Information: ")
    for port in range(75, 86):
        scan_port(ip_addr, port)


#This is for scan the port indvidually
#port = 80
#check_ip(ip_addr)
#for port in range(75, 85+1):
#    scan_port(ip_addr, port)

#This was a test to prove if it get the ip address
#print(socket.gethostbyname(ip_addr)

