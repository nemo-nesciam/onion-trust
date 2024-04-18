#config
import socket
some_variable = 'example data'
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
