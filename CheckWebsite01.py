import socket
import urllib.request

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# Check status of website
print('TASK [Check status of website]' + ' ' + (20 * '*'))
address = 'http://' + get_ip()
try:
    status = urllib.request.urlopen(address).getcode()
    if status == 200:
        print('Website is up.')
        print('True')
    else:
        print('Website appears to be down.')
        print('False')
except:
    print('Website appears to be down.')
    print('False')