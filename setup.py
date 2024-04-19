#config
import hashlib
print('Checking Tor status...')
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
