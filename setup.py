#config
some_variable = 'example data'
import stem.control
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
