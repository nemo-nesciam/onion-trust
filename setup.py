Wed Apr 17 16:29:05 BST 2024
import requests; response = requests.get('http://check.torproject.org/', proxies={'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}); print(response.text)
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
