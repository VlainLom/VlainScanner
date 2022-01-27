import socket
#pip install IPy
#pip3 install IPy
from IPy import IP

def scan(target):
    converted_ip =check_ip(target)
    print("\n" + "[+] Analyse de [ " + str(target) + ' ]')
    for port in range(1,10001):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)

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

print('Saisissez les cibles à analyser')
targets = input('>>> ')
if ' ' in targets:
    for ip_add in targets.split(' '):
        scan(ip_add.strip(' '))
else:
    scan(targets)