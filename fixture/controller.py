from fixture.client_ import Client
from fixture.register.api import Register


class Controller:
    def __init__(self, url):
        self.url = url
        self.register = Register(self)
        self.client = Client
