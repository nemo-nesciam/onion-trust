#config
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
print('Checking Tor status...')
