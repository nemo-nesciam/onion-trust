#config
print('Checking Tor status...')
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
print('Checking Tor status...')
