#config
import requests
import stem.control; with stem.control.Controller.from_port() as controller: controller.authenticate(); print('Tor is running' if controller.is_alive() else 'Tor is not running')
import stem.control
