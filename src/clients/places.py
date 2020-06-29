from src.clients import BaseClient


class PlacesClient(BaseClient):

    def __init__(self, version='v1'):
        super(PlacesClient, self).__init__('places', version=version)