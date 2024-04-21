#config
import socks
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
import hashlib
