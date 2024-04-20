#config
some_variable = 'example data'
import socks
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
