#config
print(f'Hash of the variable:', hashlib.sha256(some_variable.encode()).hexdigest())
import hashlib
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
