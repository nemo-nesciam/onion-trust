#config
import socket; socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050); socket.socket = socks.socksocket; print('Sockets redirected over Tor')
import hashlib
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
