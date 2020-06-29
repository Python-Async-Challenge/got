from src.clients import BaseClient


class PeopleClient(BaseClient):
    
    def __init__(self, version='v1'):
        super(PeopleClient, self).__init__('people', version=version)
