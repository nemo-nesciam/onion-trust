#config
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import socket
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
