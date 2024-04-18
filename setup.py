#config
some_variable = 'example data'
print('Checking Tor status...')
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
