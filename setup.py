#config
some_variable = 'example data'
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import stem.control
