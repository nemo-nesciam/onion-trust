#config
some_variable = 'example data'
import requests
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
