import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)

print('Entrer adresse ip cible')
ipaddress = input('>>> ')
converted_ip = check_ip(ipaddress)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Le Port '+ str(port) +' est Ouvert ! | ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Le Port ' + str(port) + ' est Ouvert !')
    except:
        pass

for port in range(1,1001):
    scan_port(converted_ip, port)